from multiprocessing import Pool
from sage.misc.prandom import randint
from sys import argv

def mr_primality(n: int, k: int, a: int = 0) -> bool:
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
    r = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        r += 1

    def composite(a: int) -> bool:
        if power_mod(a, d, n) == 1:
            return False
        for i in range(r):
            if power_mod(a, (2^i)*d, n) == n - 1:
                return False
        return True

    for _ in range(k):
        if a == 0:
            a = randint(2, n)
        if composite(a):
            return False
    return True

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
                mr_res = mr_primality(n, k) # passing all random bases
            elif len(argv) >= 2:
                mr_res = mr_primality(n, k, int(argv[1])) # passing a specific base
            if len(argv) == 3:
                mr_res_2 = mr_primality(n, k, int(argv[2]))
            if len(argv) < 3:
                if mr_res and not is_prime:
                    print(f"Miller Rabin pseudoprime: {n}, tries: {k}")
                    pprimes += 1
            else:
                if mr_res and mr_res_2 and not is_prime: # for passing 2 bases together
                    # Miller Rabin primality returns True, Sage returns False => pseudoprime
                    print(f"Miller Rabin pseudoprime: {n}, tries: {k}")
                    pprimes += 1
        result += pprimes
    return numerical_approx(result / 3., digits=2)


if __name__ == "__main__":
    print(argv)
    with Pool(4) as p:
        results = {k: average_pprimes(k) for k in range(1, 100)}
    print(results)
    # lowest number of tries for lowest number of pseudoprimes
    print(sorted(results.items(), key=lambda x: x[1])[0])

