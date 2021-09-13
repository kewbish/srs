from numba import njit, vectorize
import numpy as np
from random import randint
from sympy import isprime


@njit(fastmath=True)
def power_mod(b: int, e: int, n: int) -> int:
    if n == 1:
        return 0
    res = 1
    b = b % n
    while e > 0:
        if e % 2 == 1:
            res = (res * b) % n
        e = e // 2
        b = (b * b) % n
    return res


@njit(fastmath=True)
def composite(a: int, d: int, n: int, r: int) -> bool:
    if power_mod(a, d, n) == 1:
        return False
    for i in range(r):
        if power_mod(a, (2 ^ i) * d, n) == n - 1:
            return False
    return True


@vectorize
def mr_primality(n: int, k: int, arga: int = 0) -> bool:
    """
    Returns True if number is probably prime.
    Returns False if number is composite.
    """
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False

    r = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        r += 1

    for _ in range(k):
        a = randint(2, n) if arga == 0 else arga
        if composite(a, d, n, r):
            return False
    return True
