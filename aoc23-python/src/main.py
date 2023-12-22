from day8.solver import Day8Solver

filename: str = "day8.txt"
# solver: Day7Solver = Day7Solver.create(filename, isTestFile=True, use_joker=False)

solver: Day8Solver = Day8Solver(filename, isTestFile=False)
# solver.run_task1()
solver.run_task2()
