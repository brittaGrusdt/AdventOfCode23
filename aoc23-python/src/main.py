from day9.solver import Day9Solver

filename: str = "day9.txt"
# solver: Day7Solver = Day7Solver.create(filename, isTestFile=True, use_joker=False)

solver: Day9Solver = Day9Solver(filename, isTestFile=False)
solver.run_task1()
solver.run_task2()
