from collections import defaultdict
from multiprocessing import Pool
from sage.misc.prandom import randint

def euler_primality(n: int, k: int, a: int = 0) -> bool:
    """
    Returns True if number is probably prime.
    Returns False if number is composite.
    """
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    for _ in range(k):
        if a == 0:
            a = randint(2, n - 2)
        expted = power_mod(a, (n - 1) // 2, n)
        if expted != jacobi_symbol(a, n):
            return False
    return True

def gen_randints() -> list[tuple[int, bool]]:
    randints = []
    for _ in range(10^3):
        rand = randint(1000000, 2000000)
        sage_rand = is_prime(rand)
        randints.append((rand, sage_rand))
    return randints

def average_pprimes(k) -> float:
    result = 0
    for _ in range(3):
        pprimes = 0
        for n, is_prime in gen_randints():
            # euler_res = euler_primality(n, k) # passing all random bases
            # euler_res = euler_primality(n, k, 5) # passing a specific base
            euler_res_1 = euler_primality(n, k, 2)
            euler_res_2 = euler_primality(n, k, 5)
            # if euler_res and not is_prime: # for passing 1 base
            if euler_res_1 and euler_res_2 and not is_prime: # for passing 2 bases together
                # Euler primality returns True, Sage returns False => pseudoprime
                print(f"Euler pseudoprime: {n}, tries: {k}")
                pprimes += 1
        result += pprimes
    return numerical_approx(result / 3., digits=2)

if __name__ == "__main__":
    with Pool(50) as p:
        results = {k: average_pprimes(k) for k in range(1, 100)}
    print(results)
    # lowest number of tries for lowest number of pseudoprimes
    print(sorted(results.items(), key=lambda x: x[1])[0])

