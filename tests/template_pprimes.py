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
            res = fn(n, k, 0)  # passing all random bases
        elif len(argv) >= 2:
            res = fn(n, 1, int(argv[1]))  # passing a specific base
        if len(argv) == 3:
            res_2 = fn(n, 1, int(argv[2]))
        if len(argv) < 3:
            if res and not isprime(n):  # for passing 1 base
                pprimes += 1
        else:
            if res and res_2 and not isprime(n):  # for passing 2 bases together
                pprimes += 1
    return pprimes
