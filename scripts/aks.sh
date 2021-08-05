#!/bin/bash

:> aks_results.txt
(time python ../tests/aks_pseudoprimes.py) &>> aks_results.txt
