from sage.misc.prandom import randint
from typing import Union

def euler_primality(n: int, k: int, a: int = 0) -> Union[bool, tuple[bool, int]]:
    """
    Returns True if number is probably prime.
    Returns False if number is composite.
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
            return False
    return True

if __name__ == "__main__":
    for n in range(1, 10^4):
        euler_res = euler_primality(n, 20)
        sage_res = is_prime(n)
        if not euler_res:
            # Euler composite
            print(f"Composite: {n}, witness: {euler_res[1]}")
        elif euler_res and not sage_res:
            # Euler primality returns True, Sage returns False
            print(f"Euler pseudoprime: {n}")
        elif euler_res:
            # Euler primality True
            print(f"Prime: {n}, Sage: {sage_res}, Fermat: {euler_res}")

