from aks_primality import aks_probablistic, aks_primality
from numba import njit, vectorize
import numpy as np
from random import randrange
from sympy import isprime
from sys import argv
from timeit import default_timer, timeit


@njit
def gen_randints() -> np.ndarray:
    return np.array([randrange(10 ** 5 + 1, 10 ** 6 + 1, 2) for _ in range(10 ** 2)])


def aks_pprimes(k) -> float:
    pprimes = 0
    print(k)
    for n in gen_randints():
        res = aks_probablistic(n, k)
        if res and not isprime(n):
            pprimes += 1
    return pprimes


if __name__ == "__main__":

    def main():
        start = default_timer()
        print(argv)
        ints = np.arange(1, 11)
        results = np.array([aks_pprimes(n) for n in ints])
        print(repr(results))
        print(round(np.average(results), 4))
        print((ints[np.argmin(results)], np.min(results)))
        end = default_timer()
        m, s = divmod(end - start, 60)
        print(f"{round(m)}m{round(s, 4)}s")
        print("\n")

    def time_main():
        results = np.array([timeit(lambda: aks_pprimes(k), number=15) for k in range(1, 20)])
        print(repr(results))
        print(",".join([str(r) for r in results]))

    main()
