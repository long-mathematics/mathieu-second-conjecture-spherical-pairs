#!/usr/bin/env python3
"""Exact finite checks supporting the spherical-classification draft.

These checks do not prove the infinite moment identities or branching rules.
The manuscript supplies those proofs / precise external references.
Requires Python >= 3.10 and SymPy.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial
import sympy as sp

U, V, S = sp.symbols('U V S')
R = S*(U+2)*(2-S*(U**2+2*U+2))
P = sp.expand((1+U)*(V-R))
assert sp.expand((1-S)**2-U*R-(1-(1+U)**2*S)**2) == 0
print('Normalizer circuit: polynomial identity verified exactly.')

Poly = dict[tuple[int, int, int], int]
terms: Poly = {tuple(e): int(c) for e,c in sp.Poly(P,U,V,S).terms()}

def multiply(a: Poly, b: Poly) -> Poly:
    out = defaultdict(int)
    for (a0,a1,a2),ca in a.items():
        for (b0,b1,b2),cb in b.items():
            out[a0+b0,a1+b1,a2+b2] += ca*cb
    return {e:c for e,c in out.items() if c}

@lru_cache(None)
def sphere_monomial(a: int, b: int, c: int) -> Fraction:
    # U=u^2, V=v^2, S=t^2. Phase averaging kills a!=b.
    # For a=b, the integral is int_0^1 (1-t^2)^(2a) t^(2c) dt.
    if a != b:
        return Fraction(0)
    return sum((Fraction((-1)**j*comb(2*a,j), 2*c+2*j+1)
                for j in range(2*a+1)), Fraction(0))

power: Poly = {(0,0,0):1}
checks = 0
for m in range(1,13):
    power = multiply(power,terms)
    c2m = Fraction(4**(2*m)*factorial(2*m)**2, factorial(4*m+1))
    values = []
    for mark in range(m+3):
        got = sum((coef*sphere_monomial(a+mark,b,c)
                   for (a,b,c),coef in power.items()), Fraction(0))
        expected = c2m*comb(m-1,mark-1) if 1 <= mark <= m else Fraction(0)
        assert got == expected, (m,mark,got,expected)
        checks += 1
        if mark <= 1:
            values.append(str(got))
    print(f'm={m:2d}: h(P^m)={values[0]}, h(U P^m)={values[1]}')
print(f'Normalizer direct monomial integrations: {checks} checks passed.')

# Check the selected interlacing summands and dimensions independently
# against the Weyl dimension formula, for bounded highest weights.
a2_count = 0
for a in range(31):
    for b in range(31):
        if a == b == 0:
            continue
        lam = (a+b,b,0)
        mu = (b,b-1) if b else (1,0)
        assert lam[0] >= mu[0] >= lam[1] >= mu[1] >= lam[2]
        assert mu[0]-mu[1] == 1
        branch_dim = sum(x-y+1 for x in range(b,a+b+1) for y in range(b+1))
        assert 2*branch_dim == (a+1)*(b+1)*(a+b+2)
        a2_count += 1
print(f'A2 interlacing selections and dimension checks: {a2_count} passed.')

b2_count = 0
for aa in range(1,41):
    for bb in range(aa%2,aa+1,2):
        a,b = Fraction(aa,2),Fraction(bb,2)
        c,d = (b,b-1) if b else (Fraction(1),Fraction(0))
        assert a >= c >= b >= abs(d)
        assert c-d == 1 and (a-c).denominator == (b-d).denominator == 1
        branch_dim = sum((Fraction(cc,2)-Fraction(dd,2)+1)
                         *(Fraction(cc,2)+Fraction(dd,2)+1)
                         for cc in range(bb,aa+1,2)
                         for dd in range(-bb,bb+1,2))
        weyl_dim = (a-b+1)*(a+b+2)*(2*a+3)*(2*b+1)/6
        assert branch_dim == weyl_dim
        b2_count += 1
print(f'B2 integral/spin interlacing selections and dimension checks: {b2_count} passed.')
print('All checks passed. These finite checks are supplementary, not a formal verification.')
