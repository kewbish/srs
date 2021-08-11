from aks_primality import aks_probablistic
from euler_primality import euler_primality
from fermat_primality import fermat_primality
from mr_primality import mr_primality
import numpy as np
from sympy import isprime
from timeit import default_timer

if __name__ == "__main__":

    def main():
        start = default_timer()
        ints = np.arange(10 ** 5, 10 ** 6)
        print(ints.tolist())
        primes = np.vectorize(isprime)(ints)
        print(primes.tolist())
        aks_res = np.array([aks_probablistic(n, 1) for n in ints])
        print(ints[np.logical_and(aks_res, np.logical_not(primes))].tolist())
        print(ints[np.logical_and(aks_res, np.logical_not(primes))].tolist())
        end = default_timer()
        m, s = divmod(end - start, 60)
        print(f"{round(m)}m{round(s, 4)}s")
        start = default_timer()
        euler_res = np.array([euler_primality(n, 1, 0) for n in ints])
        print(ints[np.logical_and(euler_res, np.logical_not(primes))].tolist())
        print(ints[np.logical_and(euler_res, np.logical_not(primes))].tolist())
        end = default_timer()
        m, s = divmod(end - start, 60)
        print(f"{round(m)}m{round(s, 4)}s")
        start = default_timer()
        fermat_res = np.array([fermat_primality(n, 1, 0) for n in ints])
        print(ints[np.logical_and(fermat_res, np.logical_not(primes))].tolist())
        print(ints[np.logical_and(fermat_res, np.logical_not(primes))].tolist())
        end = default_timer()
        m, s = divmod(end - start, 60)
        print(f"{round(m)}m{round(s, 4)}s")
        start = default_timer()
        mr_res = np.array([mr_primality(n, 1, 0) for n in ints])
        print(ints[np.logical_and(mr_res, np.logical_not(primes))].tolist())
        print(ints[np.logical_and(mr_res, np.logical_not(primes))].tolist())
        end = default_timer()
        m, s = divmod(end - start, 60)
        print(f"{round(m)}m{round(s, 4)}s")

    main()
