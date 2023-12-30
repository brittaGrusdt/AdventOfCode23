import pathlib

from ..utils.solver import compute_path_to_input_file
from .solver import Day6Solver

path_to_input_file: pathlib.Path = compute_path_to_input_file(__file__)
solver: Day6Solver = Day6Solver(path_to_input_file)
solver.run_task1()
solver.run_task2()
