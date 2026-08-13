#!/usr/bin/env python3
"""Bounded checks for the 5-rank counterexample/boundary audit.

This file deliberately uses only Python's standard library.  It enumerates
primitive reduced positive-definite binary quadratic forms of a negative
fundamental discriminant and composes them through the corresponding ideals.
Thus it can measure the kernel of multiplication by 5 in the imaginary
quadratic class group without PARI/GP, Sage, or Magma.

This is finite evidence, not a proof about the asymptotic counting function.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from functools import reduce
from math import gcd, isqrt

Form = tuple[int, int, int]


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return abs(a), 1 if a >= 0 else -1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y


def bezout_list(values: list[int]) -> tuple[int, list[int]]:
    """Return g and coefficients c with sum(c_i values_i) = g >= 0."""
    g = 0
    coefficients: list[int] = []
    for value in values:
        new_g, x, y = extended_gcd(g, value)
        coefficients = [x * coefficient for coefficient in coefficients] + [y]
        g = new_g
    return g, coefficients


def lattice_basis(generators: list[tuple[int, int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    """Hermite-style basis for the rank-two Z-lattice spanned by generators."""
    determinant_gcd = reduce(
        gcd,
        (
            abs(generators[j][0] * generators[i][1] - generators[j][1] * generators[i][0])
            for i in range(len(generators))
            for j in range(i)
        ),
        0,
    )
    q, coefficients = bezout_list([y for _, y in generators])
    q = abs(q)
    if determinant_gcd == 0 or q == 0:
        raise ValueError("generators do not span a rank-two lattice")
    x = sum(coefficient * generator[0] for coefficient, generator in zip(coefficients, generators))
    y = sum(coefficient * generator[1] for coefficient, generator in zip(coefficients, generators))
    if y == -q:
        x, y = -x, q
    assert y == q
    p = determinant_gcd // q
    return (p, 0), (x % p, q)


def reduce_form(form: Form) -> Form:
    """Gauss-reduce a positive-definite form [a,b,c]."""
    a, b, c = form
    for _ in range(100):
        shift = (a - b) // (2 * a)
        if shift:
            c = a * shift * shift + b * shift + c
            b = b + 2 * a * shift
        if a > c:
            a, b, c = c, -b, a
            continue
        if -a < b <= a and a <= c:
            if (abs(b) == a or a == c) and b < 0:
                b = -b
            return a, b, c
    raise RuntimeError(f"form reduction did not terminate: {form}")


def compose(left: Form, right: Form, discriminant: int) -> Form:
    """Compose forms by multiplying their oriented quadratic-order ideals."""
    a1, b1, _ = left
    a2, b2, _ = right
    parity = discriminant & 1
    omega_norm = (parity * parity - discriminant) // 4
    q1 = (b1 - parity) // 2
    q2 = (b2 - parity) // 2

    # In the basis (1, omega), omega^2 = parity*omega - omega_norm.
    generators = [
        (a1 * a2, 0),
        (a1 * q2, a1),
        (a2 * q1, a2),
        (q1 * q2 - omega_norm, parity + q1 + q2),
    ]
    v1, v2 = lattice_basis(generators)
    determinant = v1[0] * v2[1] - v1[1] * v2[0]
    if determinant < 0:
        v1, v2 = v2, v1
        determinant = -determinant

    def norm(vector: tuple[int, int]) -> int:
        x, y = vector
        return x * x + parity * x * y + omega_norm * y * y

    a = norm(v1) // determinant
    c = norm(v2) // determinant
    b = (
        2 * v1[0] * v2[0]
        + parity * (v1[0] * v2[1] + v2[0] * v1[1])
        + 2 * omega_norm * v1[1] * v2[1]
    ) // determinant
    assert b * b - 4 * a * c == discriminant
    return reduce_form((a, b, c))


def reduced_forms(discriminant: int) -> list[Form]:
    forms: list[Form] = []
    for a in range(1, isqrt(abs(discriminant) // 3) + 2):
        for b in range(-a, a + 1):
            if (b - discriminant) % 2:
                continue
            numerator = b * b - discriminant
            if numerator % (4 * a):
                continue
            c = numerator // (4 * a)
            if a > c:
                continue
            if (abs(b) == a or a == c) and b < 0:
                continue
            if gcd(gcd(a, abs(b)), c) > 1:
                continue
            forms.append((a, b, c))
    return forms


def is_squarefree(value: int) -> bool:
    value = abs(value)
    prime = 2
    while prime * prime <= value:
        if value % (prime * prime) == 0:
            return False
        prime += 1
    return True


def is_negative_fundamental_discriminant(discriminant: int) -> bool:
    if discriminant >= 0:
        return False
    if discriminant % 4 == 1:
        return is_squarefree(discriminant)
    if discriminant % 4 == 0:
        radicand = discriminant // 4
        return radicand % 4 in (2, 3) and is_squarefree(radicand)
    return False


def power(form: Form, exponent: int, discriminant: int) -> Form:
    parity = discriminant & 1
    identity = (1, parity, (parity * parity - discriminant) // 4)
    result = identity
    while exponent:
        if exponent & 1:
            result = compose(result, form, discriminant)
        form = compose(form, form, discriminant)
        exponent //= 2
    return result


def five_rank_data(discriminant: int) -> tuple[int, int, int]:
    forms = reduced_forms(discriminant)
    parity = discriminant & 1
    identity = (1, parity, (parity * parity - discriminant) // 4)
    killed_by_five = sum(power(form, 5, discriminant) == identity for form in forms)
    rank = 0
    quotient = killed_by_five
    while quotient > 1 and quotient % 5 == 0:
        quotient //= 5
        rank += 1
    assert quotient == 1
    return len(forms), killed_by_five, rank


def check_hlp_sample() -> None:
    """Check equation (2.3) and nondegeneracy a != 0 for the paper's sample."""
    t, u, z = Fraction(2, 3), Fraction(-1, 3), Fraction(25)

    def delta5(value: Fraction) -> Fraction:
        return (2 * value - 1) ** 5 * (4 * value * value - 2 * value - 1)

    left = delta5(t) * z * z
    right = delta5(u)
    a = 2 * (
        8 * t**6 * z
        - 32 * t**5 * z
        + 40 * t**4 * z
        - 20 * t**3 * z
        + 4 * t * z
        - 8 * u**6
        + 32 * u**5
        - 40 * u**4
        + 20 * u**3
        - 4 * u
        - z
        + 1
    )
    assert left == right and a != 0
    print(f"HLP sample: equation(2.3) sides={left}; a={a}; status=passed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=50_000)
    args = parser.parse_args()
    if args.bound < 4:
        raise SystemExit("--bound must be at least 4")

    # Small exact values guard the enumeration and group law.
    assert [len(reduced_forms(d)) for d in (-3, -4, -23)] == [1, 1, 3]
    identity_23 = reduced_forms(-23)[0]
    assert all(power(form, 3, -23) == identity_23 for form in reduced_forms(-23))
    print("sanity: h(-3)=1, h(-4)=1, Cl(-23) has order 3; status=passed")
    check_hlp_sample()

    hits: list[tuple[int, int, int, int]] = []
    divisible_but_rank_lt_two: list[tuple[int, int, int, int]] = []
    fundamental_count = 0
    for discriminant in range(-3, -args.bound - 1, -1):
        if not is_negative_fundamental_discriminant(discriminant):
            continue
        fundamental_count += 1
        forms = reduced_forms(discriminant)
        class_number = len(forms)
        if class_number % 25:
            continue
        class_number, kernel_size, rank = five_rank_data(discriminant)
        record = (discriminant, class_number, kernel_size, rank)
        if rank >= 2:
            hits.append(record)
        else:
            divisible_but_rank_lt_two.append(record)

    print(f"scope: negative fundamental discriminants -{args.bound} <= D < 0; count={fundamental_count}")
    print(f"rank>=2 records: count={len(hits)}")
    for discriminant, class_number, kernel_size, rank in hits:
        print(f"  D={discriminant} h={class_number} |Cl[5]|={kernel_size} 5-rank={rank}")
    if hits:
        print(f"first_by_abs_discriminant: D={hits[0][0]}")

    print(f"25|h but 5-rank<2 records: count={len(divisible_but_rank_lt_two)}")
    for discriminant, class_number, kernel_size, rank in divisible_but_rank_lt_two[:10]:
        print(f"  D={discriminant} h={class_number} |Cl[5]|={kernel_size} 5-rank={rank}")
    if len(divisible_but_rank_lt_two) > 10:
        print(f"  ... {len(divisible_but_rank_lt_two) - 10} further records omitted")

    print("finite_search_conclusion=not_refuted_within_scope")


if __name__ == "__main__":
    main()
