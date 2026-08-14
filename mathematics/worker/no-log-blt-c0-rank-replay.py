#!/usr/bin/env python3
"""Exact rational replay for the BLT Theorem 2.1 sample and C0 model."""

from fractions import Fraction as Q
from math import comb, gcd, isqrt, lcm


def add(p, q):
    r = [Q(0)] * max(len(p), len(q))
    for i, value in enumerate(p):
        r[i] += value
    for i, value in enumerate(q):
        r[i] += value
    return r


def mul(p, q):
    r = [Q(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i + j] += x * y
    return r


def power(p, n):
    r = [Q(1)]
    for _ in range(n):
        r = mul(r, p)
    return r


def primitive_integer_polynomial(p):
    denominator = 1
    for x in p:
        denominator = lcm(denominator, x.denominator)
    integers = [int(x * denominator) for x in p]
    content = 0
    for x in integers:
        content = gcd(content, abs(x))
    return [x // content for x in integers], Q(content, denominator)


t, u, z = Q(2, 3), Q(-1, 3), Q(25)

# BLT (2.3).
lhs = (2 * t - 1) ** 5 * (4 * t**2 - 2 * t - 1) * z**2
rhs = (2 * u - 1) ** 5 * (4 * u**2 - 2 * u - 1)
assert lhs == rhs == Q(-3125, 2187)

# BLT Theorem 2.1, pp. 4--5.  The variable names match the paper.
a = 2 * (
    8 * t**6 * z - 32 * t**5 * z + 40 * t**4 * z - 20 * t**3 * z
    + 4 * t * z - 8 * u**6 + 32 * u**5 - 40 * u**4 + 20 * u**3
    - 4 * u - z + 1
)
a0 = -64 * t**5 * (t - 1) ** 5 * (t**2 - 3 * t + 1)
a2 = 2 * (
    32*t**12*z - 256*t**11*z + 832*t**10*z - 1440*t**9*z
    + 1440*t**8*z - 960*t**7*z + 64*t**6*u**6 - 256*t**6*u**5
    + 320*t**6*u**4 - 160*t**6*u**3 + 32*t**6*u + 640*t**6*z
    - 8*t**6 - 256*t**5*u**6 + 1024*t**5*u**5 - 1280*t**5*u**4
    + 640*t**5*u**3 - 128*t**5*u - 480*t**5*z + 32*t**5
    + 320*t**4*u**6 - 1280*t**4*u**5 + 1600*t**4*u**4
    - 800*t**4*u**3 + 160*t**4*u + 240*t**4*z - 40*t**4
    - 160*t**3*u**6 + 640*t**3*u**5 - 800*t**3*u**4
    + 400*t**3*u**3 - 80*t**3*u - 40*t**3*z + 20*t**3 - 16*t**2*z
    + 32*t*u**6 - 128*t*u**5 + 160*t*u**4 - 80*t*u**3 + 16*t*u
    + 8*t*z - 4*t - 8*u**6 + 32*u**5 - 40*u**4 + 20*u**3
    - 4*u - z + 1
)
a4 = (
    384*t**7*z**2 - 128*t**6*u**6*z + 512*t**6*u**5*z
    - 640*t**6*u**4*z + 320*t**6*u**3*z - 64*t**6*u*z
    - 1152*t**6*z**2 + 16*t**6*z + 512*t**5*u**6*z
    - 2048*t**5*u**5*z + 2560*t**5*u**4*z - 1280*t**5*u**3*z
    + 256*t**5*u*z + 1344*t**5*z**2 - 64*t**5*z
    - 640*t**4*u**6*z + 2560*t**4*u**5*z - 3200*t**4*u**4*z
    + 1600*t**4*u**3*z - 320*t**4*u*z - 720*t**4*z**2 + 80*t**4*z
    + 320*t**3*u**6*z - 1280*t**3*u**5*z + 1600*t**3*u**4*z
    - 800*t**3*u**3*z + 160*t**3*u*z + 120*t**3*z**2 - 40*t**3*z
    + 48*t**2*z**2 - 64*t*u**6*z + 256*t*u**5*z - 320*t*u**4*z
    + 160*t*u**3*z - 32*t*u*z - 24*t*z**2 + 8*t*z - 64*u**12
    + 512*u**11 - 1664*u**10 + 2880*u**9 - 2880*u**8 + 1536*u**7
    + 16*u**6*z - 128*u**6 - 64*u**5*z - 384*u**5 + 80*u**4*z
    + 240*u**4 - 40*u**3*z - 40*u**3 - 16*u**2 + 8*u*z + 8*u
    + 3*z**2 - 2*z - 1
)
a6 = z * (
    -128*t**7*z**2 + 384*t**6*z**2 - 448*t**5*z**2
    + 240*t**4*z**2 - 40*t**3*z**2 - 16*t**2*z**2 + 8*t*z**2
    + 64*u**12 - 512*u**11 + 1664*u**10 - 2880*u**9 + 2880*u**8
    - 1536*u**7 + 128*u**6 + 384*u**5 - 240*u**4 + 40*u**3
    + 16*u**2 - 8*u - z**2 + 1
)

expected = (
    Q(2048, 243), Q(-10240, 531441), Q(20480, 59049),
    Q(182272, 177147), Q(31129600, 531441),
)
assert (a, a0, a2, a4, a6) == expected
assert a != 0 and t not in (0, Q(1, 2), 1) and u not in (0, Q(1, 2), 1)

# C_even: y^2=P(x)=a(a6*x^6+a4*x^4+a2*x^2+a0).
P = [a*a0, Q(0), a*a2, Q(0), a*a4, Q(0), a*a6]
root = Q(1, 5)
assert sum(P[i] * root**i for i in range(7)) == 0

# Put X=1/(x-root), Y=y*X^3.  Then Y^2=X^6 P(root+1/X).
odd = [Q(0)] * 7
for degree, coefficient in enumerate(P):
    if coefficient:
        term = mul(power([Q(1), root], degree), [Q(0)]*(6-degree)+[Q(1)])
        odd = add(odd, [coefficient*x for x in term])
while odd and odd[-1] == 0:
    odd.pop()
odd_primitive, odd_factor = primitive_integer_polynomial(odd)
assert odd_primitive == [1900000, 2280000, 1173375, 330700, 64860, 9216]
assert odd_factor == Q(4194304, 16142520375)

# Put X=(25/6)*x0+10/3.  Direct coefficient comparison gives C0.
alpha, beta = Q(25, 6), Q(10, 3)
substituted = [Q(0)] * 6
for degree, coefficient in enumerate(odd_primitive):
    for k in range(degree + 1):
        substituted[k] += coefficient * comb(degree, k) * alpha**k * beta**(degree-k)
normalizer = Q(108, 1953125)
c0 = [2576, 8392, 11729, 8878, 3641, 640]
assert [normalizer*x for x in substituted] == c0

square_ratio = odd_factor / normalizer
assert square_ratio == Q(128000, 59049) ** 2

# Explicit birational maps between C_even and C0.
# x0=2(1-2x)/(5x-1), y0=59049*y/(1024(5x-1)^3).
# Inverse: x=(x0+2)/(5x0+4), y=8192*y0/(2187(5x0+4)^3).
# Clear all denominators and compare the forward curve equation coefficientwise:
#   1024^2*D^6*f0(N/D) = 59049^2*P(x),
# where N=2(1-2x), D=5x-1, and f0 is the C0 quintic.
N = [Q(2), Q(-4)]
D = [Q(-1), Q(5)]
forward_c0_numerator = [Q(0)] * 7
for degree, coefficient in enumerate(c0):
    term = mul(power(N, degree), power(D, 6-degree))
    forward_c0_numerator = add(
        forward_c0_numerator,
        [Q(coefficient) * value for value in term],
    )
assert [Q(1024**2) * value for value in forward_c0_numerator] == [
    Q(59049**2) * value for value in P
]

# Compose inverse x with forward x exactly. The numerator is 6*x and the
# denominator is 6, not merely equal at a finite sample of points.
inverse_x_numerator = add(N, [2 * value for value in D])
inverse_x_denominator = add(
    [5 * value for value in N],
    [4 * value for value in D],
)
assert inverse_x_numerator == [Q(0), Q(6)]
assert inverse_x_denominator == [Q(6), Q(0)]

# Since 5*x0+4=6/D, all x-dependent factors cancel in inverse_y(forward_y(y)).
inverse_y_composition_scale = (
    Q(8192, 2187) * Q(59049, 1024) / Q(6**3)
)
old_inverse_y_composition_scale = (
    Q(1024, 2187) * Q(59049, 1024) / Q(6**3)
)
assert inverse_y_composition_scale == 1
assert old_inverse_y_composition_scale == Q(1, 8)

print("equation_2_3", lhs)
print("sample_coefficients", *(str(x) for x in expected))
print("odd_primitive_coefficients", odd_primitive)
print("odd_factor", odd_factor)
print("affine_X", alpha, beta)
print("normalizer", normalizer)
print("square_ratio", square_ratio, "=", Q(128000, 59049), "^2")
print("c0_coefficients", c0)
print("forward_x0", "2*(1-2*x)/(5*x-1)")
print("forward_y0", "59049*y/(1024*(5*x-1)^3)")
print("inverse_x", "(x0+2)/(5*x0+4)")
print("inverse_y", "8192*y0/(2187*(5*x0+4)^3)")
print("forward_curve_identity", "coefficientwise exact")
print("inverse_x_composition", "exact")
print("inverse_y_composition_scale", inverse_y_composition_scale)
print("rejected_inverse_y_1024_scale", old_inverse_y_composition_scale)
print("PASS")
