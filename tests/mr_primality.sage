from sage.misc.prandom import randint

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


if __name__ == "__main__":
    for n in range(1, 10^4):
        mr_res = mr_primality(n, 20)
        sage_res = is_prime(n)
        if not mr_res:
            # Miller Rabin composite
            print(f"Composite: {n}")
        elif mr_res and not sage_res:
            # Miller Rabin primality returns True, Sage returns False
            print(f"Miller Rabin pseudoprime: {n}")
        elif mr_res:
            # Miller Rabin primality True
            print(f"Prime: {n}, Sage: {sage_res}, Fermat: {mr_res}")

