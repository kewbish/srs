from aks_primality import aks_probablistic
import numpy as np
from sympy import isprime
from sys import argv
from template_pprimes import gen_randints
from timeit import default_timer


def aks_pprimes(k) -> float:
    pprimes = 0
    for n in gen_randints():
        res = aks_probablistic(n, k)
        if res and not isprime(n):
            pprimes += 1
    return pprimes


if __name__ == "__main__":

    def main():
        start = default_timer()
        print(argv)
        ints = np.arange(1, 15)
        results = np.array([aks_pprimes(n) for n in ints])
        print(repr(results))
        print(round(np.average(results), 4))
        print((ints[np.argmin(results)], np.min(results)))
        end = default_timer()
        m, s = divmod(end - start, 60)
        print(f"{round(m)}m{round(s, 4)}s")
        print("\n")

    main()
