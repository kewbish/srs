#!/bin/bash

:> euler_results.txt
python ../../tests/euler_pseudoprimes.py &>> euler_results.txt
python ../../tests/euler_pseudoprimes.py 2 &>> euler_results.txt
python ../../tests/euler_pseudoprimes.py 3 &>> euler_results.txt
python ../../tests/euler_pseudoprimes.py 5 &>> euler_results.txt
python ../../tests/euler_pseudoprimes.py 2 3 &>> euler_results.txt
python ../../tests/euler_pseudoprimes.py 3 5 &>> euler_results.txt
python ../../tests/euler_pseudoprimes.py 2 5 &>> euler_results.txt
cd ../dataset/ && python append_csv.py euler
