from numba import njit
import numpy as np
from random import randrange
from sympy import isprime
from sys import argv


@njit
def gen_randints() -> np.ndarray:
    return np.array([randrange(10 ** 5 + 1, 10 ** 6 + 1, 2) for _ in range(10 ** 4)])


def template_pprimes(k: int, fn) -> float:
    pprimes = 0
    for n in gen_randints():
        if len(argv) == 1:
            res = fn(n, k, 0)
            if res and not isprime(n):
                pprimes += 1
    return pprimes
