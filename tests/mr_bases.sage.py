

# This file was *autogenerated* from the file mr_bases.sage
from sage.all_cmdline import *   # import sage library

_sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_4 = Integer(4); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_10 = Integer(10); _sage_const_1000000 = Integer(1000000); _sage_const_2000000 = Integer(2000000); _sage_const_3p = RealNumber('3.'); _sage_const_100 = Integer(100)
from multiprocessing import Pool
from sage.misc.prandom import randint
from sys import argv

def mr_primality(n: int, k: int, a: int = _sage_const_0 ) -> bool:
    """
    Returns True if number is probably prime.
    Returns False if number is composite.
    """
    if n == _sage_const_1  or n == _sage_const_4 :
        return False
    elif n == _sage_const_2  or n == _sage_const_3 :
        return True
    elif n % _sage_const_2  == _sage_const_0 :
        return False
    r = _sage_const_0 
    d = n - _sage_const_1 
    while d % _sage_const_2  == _sage_const_0 :
        d >>= _sage_const_1 
        r += _sage_const_1 

    def composite(a: int) -> bool:
        if power_mod(a, d, n) == _sage_const_1 :
            return False
        for i in range(r):
            if power_mod(a, (_sage_const_2 **i)*d, n) == n - _sage_const_1 :
                return False
        return True

    for _ in range(k):
        if a == _sage_const_0 :
            a = randint(_sage_const_2 , n)
        if composite(a):
            return False
    return True

def gen_randints() -> list[tuple[int, bool]]:
    randints = []
    for _ in range(_sage_const_10 **_sage_const_4 ):
        rand = randint(_sage_const_1000000 , _sage_const_2000000 )
        sage_rand = is_prime(rand)
        randints.append((rand, sage_rand))
    return randints

def average_pprimes(k) -> float:
    result = _sage_const_0 
    for _ in range(_sage_const_3 ):
        pprimes = _sage_const_0 
        for n, is_prime in gen_randints():
            if len(argv) == _sage_const_1 :
                mr_res = mr_primality(n, k) # passing all random bases
            elif len(argv) == _sage_const_2 :
                mr_res = mr_primality(n, k, int(argv[_sage_const_1 ])) # passing a specific base
            elif len(argv) == _sage_const_3 :
                mr_res_2 = mr_primality(n, k, int(argv[_sage_const_2 ]))
            if len(argv) < _sage_const_3 :
                if mr_res and not is_prime:
                    print(f"Miller Rabin pseudoprime: {n}, tries: {k}")
                    pprimes += _sage_const_1 
            else:
                if mr_res and mr_res_2 and not is_prime: # for passing 2 bases together
                    # Miller Rabin primality returns True, Sage returns False => pseudoprime
                    print(f"Miller Rabin pseudoprime: {n}, tries: {k}")
                    pprimes += _sage_const_1 
        result += pprimes
    return numerical_approx(result / _sage_const_3p , digits=_sage_const_2 )


if __name__ == "__main__":
    print(argv)
    with Pool(_sage_const_4 ) as p:
        results = {k: average_pprimes(k) for k in range(_sage_const_1 , _sage_const_100 )}
    print(results)
    # lowest number of tries for lowest number of pseudoprimes
    print(sorted(results.items(), key=lambda x: x[_sage_const_1 ])[_sage_const_0 ])


