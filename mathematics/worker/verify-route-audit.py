#!/usr/bin/env python3
"""Reproduce the inexpensive algebra checks used by construction-route-audit.md."""


def trim(poly, prime):
    result = [coefficient % prime for coefficient in poly]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def remainder(dividend, divisor, prime):
    dividend = trim(dividend, prime)
    divisor = trim(divisor, prime)
    inverse = pow(divisor[-1], -1, prime)
    while dividend != [0] and len(dividend) >= len(divisor):
        degree_shift = len(dividend) - len(divisor)
        multiplier = dividend[-1] * inverse % prime
        for index, coefficient in enumerate(divisor):
            dividend[index + degree_shift] -= multiplier * coefficient
        dividend = trim(dividend, prime)
    return dividend


def monic_gcd(left, right, prime):
    left = trim(left, prime)
    right = trim(right, prime)
    while right != [0]:
        left, right = right, remainder(left, right, prime)
    inverse = pow(left[-1], -1, prime)
    return [(coefficient * inverse) % prime for coefficient in left]


def derivative(poly):
    return [degree * poly[degree] for degree in range(1, len(poly))] or [0]


def multiply(left, right):
    product = [0] * (len(left) + len(right) - 1)
    for left_degree, left_coefficient in enumerate(left):
        for right_degree, right_coefficient in enumerate(right):
            product[left_degree + right_degree] += left_coefficient * right_coefficient
    return product


def main():
    # Coefficients are in ascending order.
    c0 = [2576, 8392, 11729, 8878, 3641, 640]
    c0_linear = [7, 5]
    c0_quartic = [368, 936, 1007, 549, 128]
    c0_product = multiply(c0_linear, c0_quartic)
    assert c0_product == c0

    byeon_quadratic = [1, 1, 1]
    byeon_sextic = [47, 261, 1198, 1561, 598, 21, 47]
    byeon_m = multiply(byeon_quadratic, byeon_sextic)

    prime = 7
    byeon_gcd = monic_gcd(byeon_m, derivative(byeon_m), prime)
    c0_gcd = monic_gcd(c0, derivative(c0), prime)
    assert byeon_gcd == [1]
    assert c0_gcd == [1]

    cross_gcd = monic_gcd(byeon_quadratic, byeon_sextic, 3)
    assert cross_gcd == [1]

    print(f"C0 factor identity: {c0_product == c0}; coefficients={c0_product}")
    print(f"Byeon Lemma 4.2 degree: {len(byeon_m) - 1}")
    print(f"gcd(Byeon m, m') over F_{prime}: {byeon_gcd}")
    print(f"gcd(C0 f, f') over F_{prime}: {c0_gcd}")
    print(f"gcd(Byeon quadratic, sextic) over F_3: {cross_gcd}")


if __name__ == "__main__":
    main()
