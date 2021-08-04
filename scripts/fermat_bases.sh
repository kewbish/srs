#!/bin/bash

:> fermat_results.txt
(time python ../tests/fermat_pseudoprimes.py) &>> fermat_results.txt
(time python ../tests/fermat_pseudoprimes.py 2) &>> fermat_results.txt
(time python ../tests/fermat_pseudoprimes.py 3) &>> fermat_results.txt
(time python ../tests/fermat_pseudoprimes.py 5) &>> fermat_results.txt
(time python ../tests/fermat_pseudoprimes.py 2 3) &>> fermat_results.txt
(time python ../tests/fermat_pseudoprimes.py 3 5) &>> fermat_results.txt
(time python ../tests/fermat_pseudoprimes.py 2 5) &>> fermat_results.txt
