from multiprocessing import Pool
from sage.misc.prandom import randint
from sys import argv
from typing import Union

def fermat_primality(n: int, k: int, a: int = 0) -> Union[bool, tuple[bool, int]]:
    """
    Returns True if number is probably prime.
    Returns False, Fermat witness or 0: int if number is composite.
    """
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False, 0
    for _ in range(k):
        if a == 0:
            a = randint(2, n - 2)
        if power_mod(a, n - 1, n) != 1:
            return False, a
    return True

def pseudoprimes(from_i: int, to_i: int, base: int) -> list[int]:
    pprimes = []
    for n in range(from_i - 1, to_i + 1):
        fermat_res = fermat_primality(n, 20, base)
        sage_res = is_prime(n)
        if type(fermat_res) == bool and not sage_res:
            pprimes.append(n)
    return pprimes

def gen_randints() -> list[tuple[int, bool]]:
    randints = []
    for _ in range(10^4):
        rand = randint(1000000, 2000000)
        sage_rand = is_prime(rand)
        randints.append((rand, sage_rand))
    return randints

def average_pprimes(k) -> float:
    result = 0
    for _ in range(3):
        pprimes = 0
        for n, is_prime in gen_randints():
            if len(argv) == 1:
                fermat_res = fermat_primality(n, k) # passing all random bases
            elif len(argv) >= 2:
                fermat_res = fermat_primality(n, k, int(argv[1])) # passing a specific base
            if len(argv) == 3:
                fermat_res_2 = fermat_primality(n, k, int(argv[2]))
            if len(argv) < 3:
                if type(fermat_res) == bool and not is_prime: # for passing 1 base
                    # print(f"Fermat pseudoprime: {n}, tries: {k}")
                    pprimes += 1
            else:
                if type(fermat_res) == bool and type(fermat_res_2) == bool and not is_prime: # for passing 2 bases together
                    # Fermat primality returns True, Sage returns False => pseudoprime
                    # print(f"Fermat pseudoprime: {n}, tries: {k}")
                    pprimes += 1
        result += pprimes
    return numerical_approx(result / 3., digits=2)

if __name__ == "__main__":
    with Pool(4) as p:
        results = {k: average_pprimes(k) for k in range(1, 100)}
    print(results)
    # lowest number of tries for lowest number of pseudoprimes
    print(sorted(results.items(), key=lambda x: x[1])[0])
