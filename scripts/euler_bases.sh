#!/bin/bash

:> euler_results.txt
(time sage ../tests/euler_bases.sage) &>> euler_results.txt
(time sage ../tests/euler_bases.sage 2) &>> euler_results.txt
(time sage ../tests/euler_bases.sage 3) &>> euler_results.txt
(time sage ../tests/euler_bases.sage 5) &>> euler_results.txt
(time sage ../tests/euler_bases.sage 2 3) &>> euler_results.txt
(time sage ../tests/euler_bases.sage 3 5) &>> euler_results.txt
(time sage ../tests/euler_bases.sage 2 5) &>> euler_results.txt
