#!/usr/bin/env python3
"""Deterministically verify the C0 finite local compatibility certificate.

This is deliberately only a finite congruence calculation.  It neither checks
the Kulkarni--Levin specialization theorem nor a Stewart--Top counting theorem.
"""

from itertools import product
from math import gcd


BAD_PRIME_EXPONENTS = {2: 4, 3: 2, 5: 2, 19: 2}
EXPECTED_DISCRIMINANT_FACTORIZATION = {2: 37, 3: 22, 5: 5, 19: 1}
RESIDUE = (-45, 1)
SIGN_SAMPLE = (-45, 1)


def quartic(u: int, v: int) -> int:
    return (
        128 * u**4
        + 549 * u**3 * v
        + 1007 * u**2 * v**2
        + 936 * u * v**3
        + 368 * v**4
    )


def form(u: int, v: int) -> int:
    return v * (5 * u + 7 * v) * quartic(u, v)


def content(coefficients: list[int]) -> int:
    result = 0
    for coefficient in coefficients:
        result = gcd(result, coefficient)
    return abs(result)


def determinant_bareiss(matrix: list[list[int]]) -> int:
    """Exact fraction-free determinant, with row swaps if needed."""
    matrix = [row[:] for row in matrix]
    size = len(matrix)
    sign = 1
    previous_pivot = 1
    for pivot_index in range(size - 1):
        if matrix[pivot_index][pivot_index] == 0:
            swap_index = next(
                index
                for index in range(pivot_index + 1, size)
                if matrix[index][pivot_index] != 0
            )
            matrix[pivot_index], matrix[swap_index] = (
                matrix[swap_index],
                matrix[pivot_index],
            )
            sign *= -1
        pivot = matrix[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    matrix[row][column] * pivot
                    - matrix[row][pivot_index] * matrix[pivot_index][column]
                )
                assert numerator % previous_pivot == 0
                matrix[row][column] = numerator // previous_pivot
        previous_pivot = pivot
    return sign * matrix[-1][-1]


def resultant(left: list[int], right: list[int]) -> int:
    """Resultant of ascending-coefficient integer polynomials."""
    left_descending = list(reversed(left))
    right_descending = list(reversed(right))
    left_degree = len(left) - 1
    right_degree = len(right) - 1
    size = left_degree + right_degree
    sylvester = []
    for shift in range(right_degree):
        sylvester.append(
            [0] * shift
            + left_descending
            + [0] * (size - shift - len(left_descending))
        )
    for shift in range(left_degree):
        sylvester.append(
            [0] * shift
            + right_descending
            + [0] * (size - shift - len(right_descending))
        )
    return determinant_bareiss(sylvester)


def discriminant(coefficients: list[int]) -> int:
    degree = len(coefficients) - 1
    derivative = [
        exponent * coefficients[exponent] for exponent in range(1, degree + 1)
    ]
    sign = -1 if degree * (degree - 1) // 2 % 2 else 1
    return sign * resultant(coefficients, derivative) // coefficients[-1]


def valuations(number: int, primes: list[int]) -> dict[int, int]:
    number = abs(number)
    result = {}
    for prime in primes:
        exponent = 0
        while number % prime == 0:
            exponent += 1
            number //= prime
        result[prime] = exponent
    assert number == 1
    return result


def squarefree_by_trial_division(number: int) -> bool:
    number = abs(number)
    prime = 2
    while prime * prime <= number:
        if number % (prime * prime) == 0:
            return False
        prime += 1
    return True


def crt(residues: list[int], moduli: list[int]) -> tuple[int, int]:
    modulus = 1
    value = 0
    for residue, local_modulus in zip(residues, moduli):
        inverse = pow(modulus, -1, local_modulus)
        step = ((residue - value) * inverse) % local_modulus
        value += modulus * step
        modulus *= local_modulus
        value %= modulus
    return value, modulus


def enumerate_local_classes(prime: int, exponent: int) -> list[tuple[int, int]]:
    modulus = prime**exponent
    classes = []
    for u, v in product(range(modulus), repeat=2):
        if gcd(gcd(u, v), prime) != 1:
            continue
        value = form(u, v)
        if prime == 2:
            # F always has a fixed factor 4 on primitive inputs.  Exact
            # v_2(F)=2 makes F/4 odd, so the reduced form has no fixed 2^2.
            if value % 16 == 4:
                classes.append((u, v))
        elif value % (prime * prime) != 0:
            classes.append((u, v))
    return classes


def main() -> None:
    # Ascending coefficients of F(u,1) = u(5+7u)Q(1,u).
    form_coefficients = [0, 640, 3641, 8878, 11729, 8392, 2576]
    discriminant_value = discriminant(form_coefficients)
    assert discriminant_value == 256083186995514939801600000
    discriminant_factorization = valuations(
        discriminant_value, sorted(EXPECTED_DISCRIMINANT_FACTORIZATION)
    )
    assert discriminant_factorization == EXPECTED_DISCRIMINANT_FACTORIZATION

    local_classes = {
        prime: enumerate_local_classes(prime, exponent)
        for prime, exponent in BAD_PRIME_EXPONENTS.items()
    }
    for classes in local_classes.values():
        assert classes

    u0, u_modulus = crt(
        [RESIDUE[0] % (prime**exponent) for prime, exponent in BAD_PRIME_EXPONENTS.items()],
        [prime**exponent for prime, exponent in BAD_PRIME_EXPONENTS.items()],
    )
    v0, v_modulus = crt(
        [RESIDUE[1] % (prime**exponent) for prime, exponent in BAD_PRIME_EXPONENTS.items()],
        [prime**exponent for prime, exponent in BAD_PRIME_EXPONENTS.items()],
    )
    assert u_modulus == v_modulus
    modulus = u_modulus

    for prime, exponent in BAD_PRIME_EXPONENTS.items():
        local_modulus = prime**exponent
        candidate = (u0 % local_modulus, v0 % local_modulus)
        assert candidate in local_classes[prime]

    assert gcd(gcd(u0, v0), modulus) == 1
    sign_value = form(*SIGN_SAMPLE)
    assert SIGN_SAMPLE[0] % modulus == u0
    assert SIGN_SAMPLE[1] % modulus == v0
    assert sign_value < 0
    assert sign_value % 4 == 0
    assert squarefree_by_trial_division(sign_value // 4)

    primitive_mod_4 = [
        (u, v) for u, v in product(range(4), repeat=2) if gcd(gcd(u, v), 2) == 1
    ]
    assert all(form(u, v) % 4 == 0 for u, v in primitive_mod_4)
    fixed_square_witnesses = {}
    for prime in BAD_PRIME_EXPONENTS:
        modulus_at_square = prime * prime
        witness = next(
            (u, v)
            for u, v in product(range(modulus_at_square), repeat=2)
            if gcd(gcd(u, v), prime) == 1
            and (
                form(u, v) % 16 == 4
                if prime == 2
                else form(u, v) % modulus_at_square != 0
            )
        )
        fixed_square_witnesses[prime] = witness

    print("C0 homogeneous sextic:")
    print("F(u,v)=v(5u+7v)(128u^4+549u^3v+1007u^2v^2+936uv^3+368v^4)")
    print(f"content(F)={content(form_coefficients)}")
    print(
        f"fixed square divisor on primitive pairs: 4 divides all "
        f"{len(primitive_mod_4)} primitive classes mod 4"
    )
    print("normalization: w=2; F/4 is an integer-valued function on primitive pairs")
    print(f"disc(F(1,x))={discriminant_value}")
    print(f"bad primes and valuations={discriminant_factorization}")
    for prime, exponent in BAD_PRIME_EXPONENTS.items():
        local_modulus = prime**exponent
        candidate = (u0 % local_modulus, v0 % local_modulus)
        candidate_value = form(*candidate) % local_modulus
        print(
            f"p={prime}: modulus={local_modulus}, admissible primitive classes="
            f"{len(local_classes[prime])}, candidate={candidate}, "
            f"F(candidate) mod {local_modulus}={candidate_value}"
        )
    print(f"bad-prime fixed-square witnesses={fixed_square_witnesses}")
    print(f"global modulus M={modulus}")
    print(f"CRT class (u0,v0)=({u0},{v0}) mod M")
    print(f"gcd(u0,v0,M)={gcd(gcd(u0, v0), modulus)}")
    print(
        f"negative sample={SIGN_SAMPLE}, F(sample)={sign_value}, "
        f"F(sample)/4={sign_value // 4}, reduced value squarefree="
        f"{squarefree_by_trial_division(sign_value // 4)}"
    )
    print("falsification outcome: survived the declared finite local checks")
    print("scope: finite bad-prime compatibility only; no thin-set, height, multiplicity, or NO-LOG proof")


if __name__ == "__main__":
    main()
