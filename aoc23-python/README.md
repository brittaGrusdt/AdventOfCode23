## aoc23-python

This folder contains my solutions implemented in Python for the Advent of Code puzzles from 2023.


### Day 5
* Task1: create a class 'Mapper'. For every mapping in the input (consisting of a header line followed by lines of respectively 3 numbers) create a Mapper instance. The Mapper stores the respective mapping ranges, i.e. destination start, source start and length as well as what is mapped to what retrieved from header line.

* Task2: 
    - first, I tried the obvious solution, simply compute the ranges and do exactly the same as in task1. For the ranges, it is important to keep range-objects since they are lazy evaluated, so that there are no huge lists stored. This worked, but took a long time to finish.
    - then, I reversed the mappings, so that I can start with the lowest possible location number (0). If the resulting original seed number is in the available ranges, that's the lowest location number we are looking for. Otherwise, test the next possible location number and go on until the resulting seed is in the original ranges. The numbers are huge, therefore this also took much time.
    - therefore: come back to this puzzle to find a more elegant solution!

### Day 6
* Task1: 

* Task2:

### Day 7
* Task1: 

* Task2:

### Day 8
* Task1: 
    - iterate through moving directions by indexing with modulo: num_iteration % len(directions), e.g. for directions = RL, start with 0 % len('RL') = 0 % 2 = 0, 1 % 2 = 1, 2 % 2 = 0, ...
    - create a dictionary mapping from node names to instances of class Node which have attributes 'left' and 'right', storing the names of the respective target nodes

* Task2:
    - now, we start with all nodes that end with 'A' simultaneously and count the number of steps needed such that for all start nodes a node ending with 'Z' is reached.
    - doing this as in task1 is too slow!
    - instead, for every start point check how many steps are needed until a circle is completed and the following steps would just be a repetition of that circle. For this purpose, save the direction, the reached node and the index of the direction-commands, e.g. for test-day8-2.txt:
    - starting at node AAA with direction commands: LLR, save the following
        - iter1: left  BBB 0
        - iter2: left  AAA 1
        - iter3: right BBB 2
        - iter4: left  AAA 0
        - iter5: left  BBB 1
        - iter6: right ZZZ 2
        - iter7: left  ZZZ 0
        - iter8: left  ZZZ 1
        - iter9: right ZZZ 2: stop here, because same has been reached after 6 iterations, so we know how it would continue from here on
    - further, remember that a node ending with 'Z' is reached after 6, 7 and 8 iterations
    - do this for all starting nodes and compute the least common multiple (lcm) of each combination of iterations, e.g. if for start node 1, after 3 and 4 iterations, nodes ending with 'Z' are reached and for start node 2 only after 2 iterations such node is reached, we take the lcm of all combinations, that is, of [2,3] and of [2,4] which are 6 and 4 respectively. From these we take the smallest one, which in this case is 4.


### Day 9
* Task1:
    - each input line of numbers as list of ints (numbers), for each do the following:
    - differences = numbers[1:] - numbers[:-1]
    - repeat subtraction until all elements of the vector differences are equal to 0, note that entries can become negative, so it is important to really check that all elements equal 0, instead of for instance checking that the sum over entries equals 0!
    - the extrapolated value for this line of numbers is the sum of all last elements of the respective input vector (numbers), the size of which is reduced after each subtraction

* Task2
    - save the first number of each line and iterate through that list from end to beginning. 
    - the extrapolated value for each line is the number from the list iterated over minus the previous extrapolated value (starting with 0)
    - logic around extrapolation is the same as for task1


### Day 11
* Task1:
    - to compute the distance, count the number of columns and rows in between each  pair of galaxies
    - thus save universe with a list of galaxies, each of which has attributes *id*, *row* and *col*

* Task2: