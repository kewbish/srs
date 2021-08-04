#!/bin/bash

:> euler_results.txt
(time python ../tests/euler_bases.py) &>> euler_results.txt
(time python ../tests/euler_bases.py 2) &>> euler_results.txt
(time python ../tests/euler_bases.py 3) &>> euler_results.txt
(time python ../tests/euler_bases.py 5) &>> euler_results.txt
(time python ../tests/euler_bases.py 2 3) &>> euler_results.txt
(time python ../tests/euler_bases.py 3 5) &>> euler_results.txt
(time python ../tests/euler_bases.py 2 5) &>> euler_results.txt
