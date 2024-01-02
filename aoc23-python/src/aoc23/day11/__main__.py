import pathlib

from ..utils.solver import compute_path_to_input_file
from .solver import Day11Solver

path_to_input_file: pathlib.Path = compute_path_to_input_file(__file__)
solver: Day11Solver = Day11Solver(path_to_input_file)
solver.run_task1()
solver.run_task2()
