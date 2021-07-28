from collections import defaultdict
from sage.misc.prandom import randint
from typing import Union

def euler_primality(n: int, k: int, a: int = 0) -> Union[bool, tuple[bool, int]]:
    """
    Returns True if number is probably prime.
    Returns False, Fermat witness: int if number is composite.
    """
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    for _ in range(k):
        if a == 0:
            a = randint(2, n - 2)
        expted = power_mod(a, (n - 1) // 2, n)
        if expted not in (1, n - 1):
            return False, a
    return True

if __name__ == "__main__":
    results = defaultdict(int)
    randints = []
    for _ in range(10^3):
        rand = randint(1000000, 2000000)
        sage_rand = is_prime(rand)
        randints.append((rand, sage_rand))
    for k in range(5, 100):
        pprimes = 0
        for _ in range(3):
            for n, is_prime in randints:
                euler_res = euler_primality(n, k)
                if type(euler_res) == bool and not is_prime:
                    # Euler primality returns True, Sage returns False
                    print(f"Euler pseudoprime: {n}, tries: {k}")
                    pprimes += 1
            results[k] += pprimes
        results[k] = numerical_approx(results[k] / 3., digits=2)
    print(results)
    print(sorted(results.items(), key=lambda x: x[1])[0])

