from math import gcd, floor
from numba import njit, vectorize
import numpy as np
from sympy import isprime


@njit
def perfectPower(n):
    """Checks if number is a power of another integer,
    if it returns true, then it is composite.
    """
    for b in range(2, int(np.log2(n)) + 1):
        a = n ** (1 / b)
        if a - int(a) == 0:
            return True
    return False


@njit
def findR(n):
    """Find smallest r such that the order of n mod r > log2(n)^2."""
    maxK = np.log2(n) ** 2
    nexR = True
    r = 1
    while nexR == True:
        r += 1
        nexR = False
        k = 0
        while k <= maxK and nexR == False:
            k = k + 1
            if fastMod(n, k, r) == 0 or fastMod(n, k, r) == 1:
                nexR = True
    return r


@njit
def fastMod(base, power, n):
    """Implement fast modular exponentiation."""
    r = 1
    while power > 0:
        if power % 2 == 1:
            r = r * base % n
        base = base ** 2 % n
        power = power // 2
    return r


@njit
def fastPoly(base, power, r):
    """Use fast modular exponentiation for polynomials to raise them to a big power."""
    x = np.zeros(len(base), dtype=np.int64)
    a = base[0]
    x[0] = 1
    n = power

    while power > 0:
        if power % 2 == 1:
            x = multi(x, base, n, r)
        base = multi(base, base, n, r)
        power = power // 2

    x[0] = x[0] - a
    x[n % r] = x[n % r] - 1
    return x


@njit
def multi(a, b, n, r):
    """Function used by fastPoly to multiply two polynomials together."""
    x = np.zeros(len(a) + len(b) - 1, dtype=np.int64)
    for i in range(len(a)):
        for j in range(len(b)):
            x[(i + j) % r] += a[(i)] * b[(j)]
            x[(i + j) % r] = x[(i + j) % r] % n
    for i in range(r, len(x)):
        x = x[:-1]
    return x


@njit
def eulerPhi(r):
    """Implement the euler phi function"""
    x = 0
    for i in range(1, r + 1):
        if gcd(r, i) == 1:
            x += 1
    return x


@vectorize
def aks_primality(n):
    """The main AKS algorithm"""
    print(n)
    if perfectPower(n) == True:  # step 1
        return False

    r = findR(n)  # step 2

    for a in range(2, min(r, n)):  # step 3
        if gcd(a, n) > 1:
            return False

    if n <= r:  # step 4
        return True

    for a in range(1, floor((eulerPhi(r)) ** (1 / 2) * np.log2(n))):
        x = fastPoly(np.array([a, 1]), n, r)
        if np.any(x):
            return False
    return True


if __name__ == "__main__":

    def main():
        ints = np.arange(3, 10 ** 4)
        aks_res = aks_primality(ints)
        sympy_res = np.vectorize(isprime)(ints)
        print(len(aks_res[np.logical_and(aks_res, np.logical_not(sympy_res))]))

    main()
