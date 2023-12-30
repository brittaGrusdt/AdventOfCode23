import pathlib
import re
from typing import Any, List

import numpy as np

from ..utils.solver import Solver


class Day9Solver(Solver):
    def __init__(self, path_to_input_file: pathlib.Path) -> None:
        super().__init__(path_to_input_file)
        self.numbers: List[List[int]] = []
        for line in self.input_lines:
            numbers: List[str] = re.split("\\s+", line)
            self.numbers.append(list(map(int, numbers)))

    def extrapolate_forward(self, values: List[int]) -> int:
        numbers: np.ndarray[int, Any] = np.asarray(values)
        extrapolated_val: int = numbers[-1]
        while sum(numbers == 0) != len(numbers):
            numbers = numbers[1:] - numbers[:-1]
            extrapolated_val += numbers[-1]

        return extrapolated_val

    def extrapolate_backward(self, values: List[int]) -> int:
        numbers: np.ndarray[int, Any] = np.asarray(values)
        first_values: List[int] = [numbers[0]]
        while sum(numbers == 0) != len(numbers):
            numbers = numbers[1:] - numbers[:-1]
            first_values.append(numbers[0])

        extrapolated_val: int = 0
        for value in first_values[-1::-1]:
            extrapolated_val = value - extrapolated_val

        return extrapolated_val

    def run_task1(self, run_forward: bool = True) -> None:
        values: List[int] = []
        for numbers in self.numbers:
            if run_forward:
                value: int = self.extrapolate_forward(numbers)
            else:
                value: int = self.extrapolate_backward(numbers)

            # print(f"numbers: {numbers}, extrapolated value: {value}")
            values.append(value)
        total_sum: int = sum(values)
        print(f"sum of all extrapolated values: {total_sum}")

    def run_task2(self) -> None:
        self.run_task1(run_forward=False)
