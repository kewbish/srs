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
def jacobi_symbol(a: int, n: int) -> int:
    a %= n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            n_mod_8 = n % 8
            if n_mod_8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    if n == 1:
        return result
    else:
        return 0


@vectorize
def euler_primality(n: int, k: int, arga: int = 0) -> bool:
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
    for _ in range(k):
        a = randint(2, n - 2) if arga == 0 else arga
        if power_mod(a, (n - 1) // 2, n) != jacobi_symbol(a, n):
            return False
    return True
