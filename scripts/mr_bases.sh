#!/bin/bash

:> mr_results.txt
(time sage ../tests/mr_bases.sage) &>> mr_results.txt
(time sage ../tests/mr_bases.sage 2) &>> mr_results.txt
(time sage ../tests/mr_bases.sage 3) &>> mr_results.txt
(time sage ../tests/mr_bases.sage 5) &>> mr_results.txt
(time sage ../tests/mr_bases.sage 2 3) &>> mr_results.txt
(time sage ../tests/mr_bases.sage 3 5) &>> mr_results.txt
(time sage ../tests/mr_bases.sage 2 5) &>> mr_results.txt
