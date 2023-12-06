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
    - For each line create an instance of class 'Game' which has an id and a set of CubeSets. Each CubeSet is a record with fields 'blue', 'green' and 'red' as once revealed, they do not change anymore.
    - For a given configuration (specific predefined CubeSet), check whether game is possible: iterate through the game's Set of CubeSets and check whether there colors that were revealed more often than in given configuration (game not possible if there are only  x red, but > x revealed)

- *Task2*:
	- For the minimal possible configuration, retrieve for each game, the maximal number of revealed cubes per color; e.g. if in one of two CubeSets, 10 red cubes are revealed and in the other 2, 10 is the minimal number of red cubes necessary for that game to be possible