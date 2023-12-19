from day7.solver import Day7Solver

filename: str = "day7.txt"
solver: Day7Solver = Day7Solver.create(filename, isTestFile=False, use_joker=False)
solver.run_task1()

solver: Day7Solver = Day7Solver.create(filename, isTestFile=False, use_joker=True)
solver.run_task2()
