#!/bin/bash

:> mr_results.txt
time sage ../tests/mr_pseudoprimes.sage >> mr_results.txt
time sage ../tests/mr_pseudoprimes.sage 2 >> mr_results.txt
time sage ../tests/mr_pseudoprimes.sage 3 >> mr_results.txt
time sage ../tests/mr_pseudoprimes.sage 5 >> mr_results.txt
time sage ../tests/mr_pseudoprimes.sage 2 3 >> mr_results.txt
time sage ../tests/mr_pseudoprimes.sage 3 5 >> mr_results.txt
time sage ../tests/mr_pseudoprimes.sage 2 5 >> mr_results.txt
