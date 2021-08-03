from numba import njit
import numpy as np
from sympy import isprime
from sys import argv


@njit
def gen_randints() -> np.ndarray:
    return np.random.randint(1000000, 2000000, size=10 ** 4)


def template_pprimes(k, fn) -> float:
    result = 0
    for _ in range(3):
        pprimes = 0
        for n in gen_randints():
            if len(argv) == 1:
                res = fn(n, k, 0)  # passing all random bases
            elif len(argv) >= 2:
                res = fn(n, k, int(argv[1]))  # passing a specific base
            if len(argv) == 3:
                res_2 = fn(n, k, int(argv[2]))
            if len(argv) < 3:
                if res and not isprime(n):  # for passing 1 base
                    # print(f"Fermat pseudoprime: {n}, tries: {k}")
                    pprimes += 1
            else:
                if res and res_2 and not isprime(n):  # for passing 2 bases together
                    # Fermat primality returns True, Symp returns False => pseudoprime
                    # print(f"Fermat pseudoprime: {n}, tries: {k}")
                    pprimes += 1
        result += pprimes
    return result / 3


if __name__ == "__main__":
    from fermat_primality import fermat_primality

    def main():
        print(argv)
        ints = np.arange(1, 100)
        results = np.array([template_pprimes(n, fermat_primality) for n in ints])
        print((ints[np.argmin(results)], np.min(results)))
        # lowest number of tries for lowest number of pseudoprimes
        # print(sorted(results.items(), key=lambda x: x[1])[0])

    main()
