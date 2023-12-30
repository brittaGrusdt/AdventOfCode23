import pathlib
import unittest

from aoc23.day9.solver import Day9Solver
from aoc23.utils.solver import compute_path_to_input_file


class TestTask1(unittest.TestCase):
    def setUp(self) -> None:
        """is run before every test method"""
        path_to_input_file: pathlib.Path = compute_path_to_input_file(__file__)
        self.solver: Day9Solver = Day9Solver(path_to_input_file)
        # TODO: here a mockup is probably better?! or is it ok to use external files for testing?

    def tearDown(self) -> None:
        """is run after each test method"""
        pass

    def test_extrapolate_forward(self) -> None:
        result1: int = self.solver.extrapolate_forward(self.solver.numbers[0])
        result2: int = self.solver.extrapolate_forward(self.solver.numbers[1])
        result3: int = self.solver.extrapolate_forward(self.solver.numbers[2])

        self.assertTrue(result1 == 18)
        self.assertTrue(result2 == 28)
        self.assertTrue(result3 == 68)
