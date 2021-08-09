from numba import njit
import numpy as np
from random import randrange
from sympy import isprime
from sys import argv
from timeit import default_timer, timeit


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
                # print(f"Fermat pseudoprime: {n}, tries: {k}")
                pprimes += 1
        else:
            if res and res_2 and not isprime(n):  # for passing 2 bases together
                # Fermat primality returns True, Symp returns False => pseudoprime
                # print(f"Fermat pseudoprime: {n}, tries: {k}")
                pprimes += 1
    return pprimes


def output(fn) -> None:
    start = default_timer()
    print(argv)
    ints = np.arange(1, 100)
    results = np.array([template_pprimes(n, fn) for n in ints])
    print(repr(results))
    print(round(np.average(results), 4))
    print((ints[np.argmin(results)], np.min(results)))
    end = default_timer()
    m, s = divmod(end - start, 60)
    print(f"{round(m)}m{round(s, 4)}s")
    print("\n")


def time_output(fn) -> None:
    print(argv)
    results = np.array([timeit(lambda: template_pprimes(k, fn), number=50) for k in range(51)])
    print(repr(results))
    print(",".join([str(r) for r in results]))


if __name__ == "__main__":
    from fermat_primality import fermat_primality

    output(fermat_primality)
