#!/bin/bash

:> fermat_results.txt
(time sage ../tests/fermat_pseudoprimes.sage) &>> fermat_results.txt
(time sage ../tests/fermat_pseudoprimes.sage 2) &>> fermat_results.txt
(time sage ../tests/fermat_pseudoprimes.sage 3) &>> fermat_results.txt
(time sage ../tests/fermat_pseudoprimes.sage 5) &>> fermat_results.txt
(time sage ../tests/fermat_pseudoprimes.sage 2 3) &>> fermat_results.txt
(time sage ../tests/fermat_pseudoprimes.sage 3 5) &>> fermat_results.txt
(time sage ../tests/fermat_pseudoprimes.sage 2 5) &>> fermat_results.txt
