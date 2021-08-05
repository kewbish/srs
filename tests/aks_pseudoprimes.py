from aks_primality import aks_primality
from numba import njit
import numpy as np
from sympy import isprime

# from template_pprimes import gen_randints


@njit
def gen_randints() -> np.ndarray:
    return np.random.randint(1000000, 2000000, size=5 * 10 ** 2)


if __name__ == "__main__":

    def main():
        ints = np.arange(3, 10 ** 4)
        aks_res = aks_primality(ints)
        sympy_res = np.vectorize(isprime)(ints)
        print(len(aks_res[np.logical_and(aks_res, np.logical_not(sympy_res))]))

    main()
