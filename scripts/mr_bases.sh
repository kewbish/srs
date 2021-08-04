#!/bin/bash

:> mr_results.txt
(time python ../tests/mr_bases.py) &>> mr_results.txt
(time python ../tests/mr_bases.py 2) &>> mr_results.txt
(time python ../tests/mr_bases.py 3) &>> mr_results.txt
(time python ../tests/mr_bases.py 5) &>> mr_results.txt
(time python ../tests/mr_bases.py 2 3) &>> mr_results.txt
(time python ../tests/mr_bases.py 3 5) &>> mr_results.txt
(time python ../tests/mr_bases.py 2 5) &>> mr_results.txt
