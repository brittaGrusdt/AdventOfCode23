# aoc23

This repository contains my solutions implemented in Java for the Advent of Code puzzles from 2023.

## Day 1

- *Task1*: for each input line retrieve list with just digits by splitting at all non-digit characters (regex: \D), take the one at the first and last position


- *Task2*: 
    - For each input line, retrieve first and last digit as in Task1. 
    
    - For each input line iterate over all digit-strings ("one", "two", ...) and check whether they are present in the input string. If yes, remember the index where it was found in the input string. If any other written out digit is present in the input string, check whether it occurs before the number that had been found before for finding the first occurrence (or after for finding the last occurrence).
    
    - Then, check whether the index of the first occurrence of the first found digit is before the first occurrence of the first found written digit, do the same for the last occurrences of found digits.

    
## Day 2

- *Task1*: 

- *Task2*: