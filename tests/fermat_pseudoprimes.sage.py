

# This file was *autogenerated* from the file fermat_pseudoprimes.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_4 = Integer(4); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_0 = Integer(0); _sage_const_20 = Integer(20); _sage_const_2000 = Integer(2000); _sage_const_5 = Integer(5)
from sage.misc.prandom import randint
from typing import Union

def fermat_primality(n: int, k: int, a: int) -> Union[bool, tuple[bool, int]]:
    """
    Returns True if number is probably prime.
    Returns False, Fermat witness: int if number is composite.
    """
    if n == _sage_const_1  or n == _sage_const_4 :
        return False
    elif n == _sage_const_2  or n == _sage_const_3 :
        return True
    elif n % _sage_const_2  == _sage_const_0 :
        return False, _sage_const_0 
    for _ in range(k):
        if power_mod(a, n - _sage_const_1 , n) != _sage_const_1 :
            return False, a
    return True

def pseudoprimes(from_i: int, to_i: int, base: int) -> list[int]:
    pprimes = []
    for n in range(from_i - _sage_const_1 , to_i + _sage_const_1 ):
        fermat_res = fermat_primality(n, _sage_const_20 , base)
        sage_res = is_prime(n)
        if type(fermat_res) == bool and not sage_res:
            pprimes.append(n)
    return pprimes

if __name__ == "__main__":
    print(pseudoprimes(_sage_const_2 , _sage_const_2000 , _sage_const_2 ))
    print(pseudoprimes(_sage_const_2 , _sage_const_2000 , _sage_const_5 ))

