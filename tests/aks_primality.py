from math import gcd, floor
from numba import njit, vectorize
import numpy as np
from random import randint
from sympy import isprime


# heavily referenced: https://github.com/Ssophoclis/AKS-algorithm/blob/master/AKS.py


@njit
def is_perfect_power(n: int) -> bool:
    for b in range(2, int(np.log2(n)) + 1):
        a = n ** (1 / b)
        if a - int(a) == 0:
            return True
    return False


@njit
def find_r(n: int) -> int:
    maxK = np.log2(n) ** 2
    nexR = True
    r = 1
    while nexR:
        r += 1
        nexR = False
        k = 0
        while k <= maxK and not nexR:
            k = k + 1
            if power_mod(n, k, r) in (0, 1):
                nexR = True
    return r


@njit
def power_mod(base: int, power: int, n: int) -> int:
    r = 1
    while power > 0:
        if power % 2 == 1:
            r = r * base % n
        base = base ** 2 % n
        power = power // 2
    return r


@njit
def poly_mod(base: np.ndarray, power: int, r: int) -> np.ndarray:
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
def multi(a: np.ndarray, b: np.ndarray, n: int, r: int) -> np.ndarray:
    x = np.zeros(len(a) + len(b) - 1, dtype=np.int64)
    for i in range(len(a)):
        for j in range(len(b)):
            x[(i + j) % r] += a[(i)] * b[(j)]
            x[(i + j) % r] = x[(i + j) % r] % n
    for i in range(r, len(x)):
        x = x[:-1]
    return x


@njit
def phi(r: int) -> int:
    x = 0
    for i in range(1, r + 1):
        if gcd(r, i) == 1:
            x += 1
    return x


@vectorize
def aks_primality(n: int) -> bool:
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False

    if is_perfect_power(n):  # step 1
        return False

    r = find_r(n)  # step 2

    for a in range(2, min(r, n)):  # step 3
        if gcd(a, n) > 1:
            return False

    if n <= r:  # step 4
        return True

    for a in range(1, r ** (1 / 2) * np.log2(n)):  # step 5
        x = poly_mod(np.array([a, 1]), n, r)
        if np.all(x):
            return True
    return False


@vectorize
def aks_probablistic(n: int, k: int) -> bool:
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False

    print(n)

    if is_perfect_power(n):  # step 1
        return False

    r = find_r(n)  # step 2

    for a in range(2, min(r, n)):  # step 3
        if gcd(a, n) > 1:
            return False

    if n <= r:  # step 4
        return True

    k_max = floor(
        r ** (1 / 2) * np.log2(n)
    )  # https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.455.5241&rep=rep1&type=pdf
    if k > k_max:
        k = k_max
    a_arr = np.random.randint(1, k_max, k)
    for a in a_arr:  # step 5
        x = poly_mod(np.array([a, 1]), n, r)
        if np.all(x):
            return True
    return False


if __name__ == "__main__":

    def main():
        ints = np.arange(3, 10 ** 4)
        # aks_res = aks_primality(ints)
        # sympy_res = np.vectorize(isprime)(ints)
        # print(len(aks_res[np.logical_and(aks_res, np.logical_not(sympy_res))]))
        aks_res = aks_probablistic(ints, 10)
        sympy_res = np.vectorize(isprime)(ints)
        print(len(aks_res[np.logical_and(aks_res, np.logical_not(sympy_res))]))

    main()
