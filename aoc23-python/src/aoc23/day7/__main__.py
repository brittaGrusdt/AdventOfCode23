import pathlib

from ..utils.solver import compute_path_to_input_file
from .solver import Day7Solver

path_to_input_file: pathlib.Path = compute_path_to_input_file(__file__)
solver: Day7Solver = Day7Solver(path_to_input_file)
solver.run_task1()

solver = Day7Solver(path_to_input_file, use_joker=True)
solver.run_task2()
