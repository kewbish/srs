from sage.misc.prandom import randint
from typing import Union

def fermat_primality(n: int, k: int, a: int) -> Union[bool, tuple[bool, int]]:
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

if __name__ == "__main__":
    print(pseudoprimes(2, 2000, 2))
    print(pseudoprimes(2, 2000, 5))
