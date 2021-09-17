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


@vectorize
def fermat_primality(n: int, k: int) -> bool:
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
        a = randint(2, n - 2)
        if power_mod(a, n - 1, n) != 1:
            return False
    return True
