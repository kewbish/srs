from sys import path

path.append("..")

import numpy as np
from sys import argv
from tests.fermat_primality import fermat_primality
from tests.euler_primality import euler_primality
from tests.mr_primality import mr_primality
from tests.aks_primality import aks_probablistic
from tests.template_pprimes import template_pprimes
from timeit import default_timer, timeit


def output(fn) -> str:
    start = default_timer()
    ints = np.arange(1, 51)
    results = np.array([template_pprimes(n, fn) for n in ints])
    end = default_timer()
    m, s = divmod(end - start, 60)
    total_time = f"{round(m)}m{round(s, 4)}s"
    results = np.append(
        results,
        [
            ints[np.argmin(results)],
            np.min(results),
            ints[np.argmax(results)].np.max(results),
            np.max(results) - np.min(results),
        ],
    )
    return ",".join([str(r) for r in results]) + f",{total_time}\n"


def time_output(fn) -> str:
    results = np.array([timeit(lambda: template_pprimes(k, fn), number=10) for k in range(51)])
    return ",".join([str(r) for r in results]) + "\n"


def csv_line(fn, pprimes: bool = True) -> str:
    """CSV format: test n (50 columns), either of pseudoprimes or time, max and min result at index, range of results, total time elapsed"""
    line = output(fn) if pprimes else time_output(fn)
    return line


def arg_parse(arg) -> None:
    def fermat():
        fermat = open("../dataset/fermat.csv", "a")
        fermat.write(csv_line(fermat_primality))

    def euler():
        euler = open("../dataset/euler.csv", "a")
        euler.write(csv_line(euler_primality))

    def mr():
        mr = open("../dataset/mr.csv", "a")
        mr.write(csv_line(mr_primality))

    def aks():
        aks = open("../dataset/aks.csv", "a")
        aks.write(csv_line(aks_probablistic))

    def all_tests():
        fermat()
        euler()
        mr()
        aks()

    cases = {"--f": fermat, "--e": euler, "--m": mr, "--a": aks, "--all": all_tests}
    cases.get(arg)()


# run the file as python generate_csv.py [num] [--f,--e,--m,--a,--all]
# num => number of runs
for _ in range(int(argv[1])):
    arg_parse(argv[2])
