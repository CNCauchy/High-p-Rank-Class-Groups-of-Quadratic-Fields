#!/usr/bin/env python3
"""Bounded falsification checks for the C0 NO-LOG candidate.

Only Python's standard library is used.  The checks are exact but finite:

* prime-power residue coverage for the binary sextic F(a,b);
* signs and fundamental-discriminant normalization in a primitive height box;
* collisions from primitive rational parameters to quadratic fields.

No successful finite check proves the NO-LOG asymptotic statement.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from math import gcd, isqrt


BAD_PRIMES = (2, 3, 5, 19)
GLOBAL_FIXED_SQUARE = 4


def quartic(a: int, b: int) -> int:
    return 128 * a**4 + 549 * a**3 * b + 1007 * a * a * b * b + 936 * a * b**3 + 368 * b**4


def binary_form(a: int, b: int) -> int:
    return b * (5 * a + 7 * b) * quartic(a, b)


def normalized_form(a: int, b: int) -> int:
    value = binary_form(a, b)
    assert value % GLOBAL_FIXED_SQUARE == 0
    return value // GLOBAL_FIXED_SQUARE


def transformed_parameters(u: int, v: int) -> tuple[int, int]:
    """Unimodular map sending the positive quadrant to -3 < a/b < -2."""
    return -2 * u - 3 * v, u + v


def transformed_form(u: int, v: int) -> int:
    return binary_form(*transformed_parameters(u, v))


def squarefree_kernel(value: int) -> int:
    if value == 0:
        return 0
    sign = -1 if value < 0 else 1
    value = abs(value)
    kernel = 1
    factors: list[int] = []
    factor_integer(value, factors)
    counts = Counter(factors)
    for prime, exponent in counts.items():
        if exponent % 2:
            kernel *= prime
    return sign * kernel


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for prime in small_primes:
        if value % prime == 0:
            return value == prime
    shift, odd = 0, value - 1
    while odd % 2 == 0:
        shift += 1
        odd //= 2
    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if base % value == 0:
            continue
        witness = pow(base, odd, value)
        if witness in (1, value - 1):
            continue
        for _ in range(shift - 1):
            witness = witness * witness % value
            if witness == value - 1:
                break
        else:
            return False
    return True


def pollard_factor(value: int) -> int:
    if value % 2 == 0:
        return 2
    if value % 3 == 0:
        return 3
    constant = 1
    while True:
        x = y = 2
        divisor = 1
        while divisor == 1:
            x = (x * x + constant) % value
            y = (y * y + constant) % value
            y = (y * y + constant) % value
            divisor = gcd(abs(x - y), value)
        if divisor != value:
            return divisor
        constant += 1


def factor_integer(value: int, factors: list[int]) -> None:
    if value == 1:
        return
    if is_prime(value):
        factors.append(value)
        return
    divisor = pollard_factor(value)
    factor_integer(divisor, factors)
    factor_integer(value // divisor, factors)


def field_discriminant_from_kernel(kernel: int) -> int:
    if kernel == 0:
        return 0
    return kernel if kernel % 4 == 1 else 4 * kernel


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def primitive_pairs_mod(modulus: int):
    for a in range(modulus):
        for b in range(modulus):
            if gcd(gcd(a, b), modulus) == 1:
                yield a, b


def local_profile(prime: int, exponent: int, *, normalized: bool) -> dict[str, object]:
    residue_modulus = prime**exponent
    # F/4 modulo 2^e depends on F modulo 2^(e+2).
    input_modulus = prime ** (exponent + (2 if normalized and prime == 2 else 0))
    square_modulus = prime * prime
    total = zero_mod_p2 = exact_v1 = squarefree_eligible = negative_residues = 0
    squarefree_by_b_nonzero = 0
    examples: dict[str, tuple[int, int, int]] = {}
    for a, b in primitive_pairs_mod(input_modulus):
        total += 1
        value = normalized_form(a, b) if normalized else binary_form(a, b)
        residue = value % residue_modulus
        v = valuation(value, prime)
        if value % square_modulus == 0:
            zero_mod_p2 += 1
        else:
            squarefree_eligible += 1
            examples.setdefault("not_p2", (a, b, residue))
        if v == 1:
            exact_v1 += 1
            examples.setdefault("v1", (a, b, residue))
        if b % prime != 0 and value % square_modulus != 0:
            squarefree_by_b_nonzero += 1
            examples.setdefault("b_unit_not_p2", (a, b, residue))
        # This is only a modular sign proxy for reporting completeness; real
        # sign is checked over integer representatives below.
        if residue > residue_modulus // 2:
            negative_residues += 1
    return {
        "prime": prime,
        "exponent": exponent,
        "residue_modulus": residue_modulus,
        "input_modulus": input_modulus,
        "primitive": total,
        "p2_divisible": zero_mod_p2,
        "eligible_not_p2": squarefree_eligible,
        "exact_v1": exact_v1,
        "eligible_b_unit": squarefree_by_b_nonzero,
        "coverage_p2": f"{zero_mod_p2}/{total}",
        "all_covered_by_p2": zero_mod_p2 == total,
        "normalized": normalized,
        "examples": examples,
    }


def joint_negative_witness(primes: tuple[int, ...], search_bound: int) -> tuple[int, int, int] | None:
    for b in range(1, search_bound + 1):
        for a in range(-search_bound, -1):
            if gcd(a, b) != 1:
                continue
            value = normalized_form(a, b)
            if value < 0 and all(value % (prime * prime) != 0 for prime in primes):
                return a, b, value
    return None


def collision_experiment(height: int) -> dict[str, object]:
    by_discriminant: dict[int, list[tuple[int, int]]] = defaultdict(list)
    zeros = positive = negative = squares = 0
    max_abs_form = 0
    primitive = 0
    fundamental_check_failures = 0
    for u in range(1, height + 1):
        for v in range(1, height + 1):
            if gcd(u, v) != 1:
                continue
            primitive += 1
            a, b = transformed_parameters(u, v)
            value = binary_form(a, b)
            max_abs_form = max(max_abs_form, abs(value))
            if value == 0:
                zeros += 1
                continue
            if value < 0:
                negative += 1
            else:
                positive += 1
            kernel = squarefree_kernel(value)
            if abs(kernel) == 1:
                squares += 1
            discriminant = field_discriminant_from_kernel(kernel)
            if discriminant % 4 not in (0, 1):
                fundamental_check_failures += 1
            by_discriminant[discriminant].append((u, v))

    multiplicities = Counter(len(parameters) for parameters in by_discriminant.values())
    max_multiplicity = max(multiplicities, default=0)
    maximal_buckets = sorted(
        (disc, params) for disc, params in by_discriminant.items() if len(params) == max_multiplicity
    )
    negative_discriminants = sum(discriminant < 0 for discriminant in by_discriminant)
    negative_parameters = sum(len(parameters) for discriminant, parameters in by_discriminant.items() if discriminant < 0)
    return {
        "height": height,
        "primitive": primitive,
        "zeros": zeros,
        "positive_values": positive,
        "negative_values": negative,
        "square_kernels": squares,
        "distinct_fields": len(by_discriminant),
        "negative_distinct_fields": negative_discriminants,
        "negative_parameters": negative_parameters,
        "max_multiplicity": max_multiplicity,
        "maximal_buckets": maximal_buckets[:5],
        "multiplicity_histogram": dict(sorted(multiplicities.items())),
        "max_abs_form": max_abs_form,
        "height_six_bound_ratio": max_abs_form / height**6,
        "fundamental_shape_failures": fundamental_check_failures,
        "distinct_per_primitive": len(by_discriminant) / primitive,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--height", type=int, default=200)
    parser.add_argument("--small-prime-max", type=int, default=43)
    args = parser.parse_args()
    if args.height < 2 or args.small_prime_max < 5:
        raise SystemExit("bounds too small")

    # Exact coefficient and obvious boundary checks.
    assert binary_form(1, 0) == 0
    assert binary_form(-7, 5) == 0
    assert binary_form(-2, 1) == -540
    assert binary_form(-3, 2) == -796
    assert gcd(abs(normalized_form(-2, 1)), abs(normalized_form(-3, 2))) == 1
    assert transformed_form(1, 0) == binary_form(-2, 1) != 0
    assert transformed_form(0, 1) == binary_form(-3, 1) != 0
    print("FORM F(a,b)=b(5a+7b)(128a^4+549a^3b+1007a^2b^2+936ab^3+368b^4)")
    print("BOUNDARY b=0 and (a,b)=(-7,5) give F=0; (-2,1),(-3,2) give negative F")
    fixed4 = local_profile(2, 2, normalized=False)
    assert fixed4["all_covered_by_p2"]
    assert all(binary_form(a, b) % 4 == 0 for a in range(4) for b in range(4))
    assert binary_form(-2, 1) % 16 != 0
    print(
        "FIXED_SQUARE raw_F all primitive classes mod 4 satisfy 4|F; "
        f"primitive={fixed4['primitive']} p2_divisible={fixed4['p2_divisible']}; "
        "all 16 residue pairs checked; F(-2,1)=-540 is not divisible by 16"
    )
    print(
        "GLOBAL_NORMALIZATION "
        f"G(-2,1)={normalized_form(-2, 1)} "
        f"G(-3,2)={normalized_form(-3, 2)} gcd_abs=1; "
        "maximal_global_w_with_w^2_dividing_every_F_value_is_w=2"
    )
    print("NORMALIZATION G(a,b)=F(a,b)/4 on primitive pairs; this is the Stewart-Top w^2 boundary")

    primes = []
    for candidate in range(2, args.small_prime_max + 1):
        if candidate > 1 and all(candidate % divisor for divisor in range(2, isqrt(candidate) + 1)):
            primes.append(candidate)
    print(
        f"LOCAL_SCOPE primes={primes}; bad_primes={list(BAD_PRIMES)}; "
        "p^2 for every listed prime, p^3 additionally for 2,3,5"
    )
    profiles = []
    for prime in primes:
        exponents = (2, 3) if prime in (2, 3, 5) else (2,)
        for exponent in exponents:
            profile = local_profile(prime, exponent, normalized=True)
            profiles.append(profile)
            print(
                "LOCAL "
                f"p={prime} e={exponent} input_mod={profile['input_modulus']} "
                f"residue_mod={profile['residue_modulus']} primitive={profile['primitive']} "
                f"p2_divisible={profile['p2_divisible']} eligible_not_p2={profile['eligible_not_p2']} "
                f"exact_v1={profile['exact_v1']} eligible_b_unit={profile['eligible_b_unit']} "
                f"all_covered_by_p2={profile['all_covered_by_p2']} examples={profile['examples']}"
            )
    assert not any(profile["all_covered_by_p2"] for profile in profiles)

    joint_primes = tuple(primes)
    joint = joint_negative_witness(joint_primes, 500)
    assert joint is not None
    print(f"LOCAL_SIGN_JOINT primes={list(joint_primes)} search_box=|a|,b<=500 negative_witness={joint}")

    heights = sorted(set((25, 50, 100, args.height)))
    for height in heights:
        collision = collision_experiment(height)
        print(
            f"COLLISION_SCOPE 1<=u,v<={height}, gcd(u,v)=1; "
            "(a,b)=(-2u-3v,u+v), so -3<a/b<-2 and F<0"
        )
        for key, value in collision.items():
            print(f"COLLISION H={height} {key}={value}")

    print("UNABSORBED_FIXED_P2_OBSTRUCTION=not_refuted_within_scope")
    print("SIGN_CONFLICT=not_refuted_within_scope")
    print("FUNDAMENTAL_DISCRIMINANT_SHAPE=passed_by_exact_normalization_within_scope")
    print("BOUNDED_COLLISION_OBSTRUCTION=not_refuted_within_scope")
    print("THIN_SET_COMPATIBILITY=not_tested_global_obligation")
    print("NO_LOG=not_proved")


if __name__ == "__main__":
    main()
