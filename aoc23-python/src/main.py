# from day5.solver import Day5Solver
from day6.solver import Day6Solver

filename: str = "day6.txt"
solver = Day6Solver(filename, isTestFile=False)

solver.run_task1()
solver.run_task2()
