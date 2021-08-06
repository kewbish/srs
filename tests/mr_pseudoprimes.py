from mr_primality import mr_primality
import numpy as np
from sys import argv
from template_pprimes import template_pprimes

if __name__ == "__main__":

    def main():
        print(argv)
        ints = np.arange(1, 100)
        results = np.array([template_pprimes(n, mr_primality) for n in ints])
        print(np.average(results))
        print((ints[np.argmin(results)], np.min(results)))
        print(np.min(results), np.max(results))

    main()
