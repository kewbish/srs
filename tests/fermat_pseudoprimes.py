from fermat_primality import fermat_primality
import numpy as np
from sys import argv
from template_pprimes import template_pprimes

if __name__ == "__main__":

    def main():
        print(argv)
        ints = np.arange(1, 100)
        results = np.array([template_pprimes(n, fermat_primality) for n in ints])
        print(np.average(results * 3))
        print((ints[np.argmin(results)], np.min(results)))

    main()
