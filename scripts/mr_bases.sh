#!/bin/bash

:> mr_results.txt
(time python ../tests/mr_pseudoprimes.py) &>> mr_results.txt
(time python ../tests/mr_pseudoprimes.py 2) &>> mr_results.txt
(time python ../tests/mr_pseudoprimes.py 3) &>> mr_results.txt
(time python ../tests/mr_pseudoprimes.py 5) &>> mr_results.txt
(time python ../tests/mr_pseudoprimes.py 2 3) &>> mr_results.txt
(time python ../tests/mr_pseudoprimes.py 3 5) &>> mr_results.txt
(time python ../tests/mr_pseudoprimes.py 2 5) &>> mr_results.txt
