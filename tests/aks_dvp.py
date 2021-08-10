from aks_primality import aks_probablistic, aks_primality
import numpy as np
from timeit import default_timer

if __name__ == "__main__":

    def main():
        start = default_timer()
        ints = np.random.randint(10 ** 5, 10 ** 6, size=10 ** 2)
        p_aks_res = np.array([aks_probablistic(n, 1) for n in ints])
        end = default_timer()
        m, s = divmod(end - start, 60)
        print(f"{round(m)}m{round(s, 4)}s")
        start = default_timer()
        d_aks_res = np.array([aks_primality(n) for n in ints])
        end = default_timer()
        m, s = divmod(end - start, 60)
        print(f"{round(m)}m{round(s, 4)}s")
        print(p_aks_res)
        print(d_aks_res)

    main()
