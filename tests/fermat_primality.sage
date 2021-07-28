from sage.misc.prandom import randint
from typing import Union

def fermat_primality(n: int, k: int) -> Union[bool, tuple[bool, int]]:
    """
    Returns True if number is probably prime.
    Returns False, Fermat witness: int if number is composite.
    """
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    for _ in range(k):
        a = randint(2, n - 2)
        if power_mod(a, n - 1, n) != 1:
            return False, a
    return True

if __name__ == "__main__":
    for n in range(1, 10^4):
        fermat_res = fermat_primality(n, 20)
        sage_res = is_prime(n)
        if type(fermat_res) == tuple and fermat_res[0] == False:
            # Fermat composite
            print(f"Composite: {n}, witness: {fermat_res[1]}")
        elif type(fermat_res) == bool and not sage_res:
            # Fermat primality returns True, Sage returns False
            print(f"Fermat liar: {n}")
        elif fermat_res:
            # Fermat primality True
            print(f"Prime: {n}, Sage: {sage_res}, Fermat: {fermat_res}")

