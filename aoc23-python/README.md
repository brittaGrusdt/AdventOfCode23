## aoc23-python

This folder contains my solutions implemented in Python for the Advent of Code puzzles from 2023.


### Day 5
* Task1: create a class 'Mapper'. For every mapping in the input (consisting of a header line followed by lines of respectively 3 numbers) create a Mapper instance. The Mapper stores the respective mapping ranges, i.e. destination start, source start and length as well as what is mapped to what retrieved from header line.

* Task2: 
    - first, I tried the obvious solution, simply compute the ranges and do exactly the same as in task1. For the ranges, it is important to keep range-objects since they are lazy evaluated, so that there are no huge lists stored. This worked, but took a long time to finish.
    - then, I reversed the mappings, so that I can start with the lowest possible location number (0). If the resulting original seed number is in the available ranges, that's the lowest location number we are looking for. Otherwise, test the next possible location number and go on until the resulting seed is in the original ranges. The numbers are huge, therefore this also took much time.
    - therefore: come back to this puzzle to find a more elegant solution!