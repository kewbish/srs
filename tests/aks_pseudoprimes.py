from aks_primality import aks_probablistic
import numpy as np
from sympy import isprime
from sys import argv
from template_pprimes import gen_randints


def aks_pprimes(k) -> float:
    pprimes = 0
    for n in gen_randints():
        res = aks_probablistic(n, k)
        if res and not isprime(n):
            pprimes += 1
    return pprimes


if __name__ == "__main__":

    def main():
        print(argv)
        results = np.array(aks_pprimes(1))
        print(np.average(results))
        print((ints[np.argmin(results)], np.min(results)))
        print(np.min(results), np.max(results))

    main()
