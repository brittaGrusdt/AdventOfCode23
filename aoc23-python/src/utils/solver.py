import pathlib
from abc import ABC, abstractmethod
from typing import List


class Solver(ABC):
    """Class defining functions for reading input from text file"""

    @abstractmethod
    def run_task1(self) -> None:
        pass

    @abstractmethod
    def run_task2(self) -> None:
        pass

    def read_input(self, path_to_file: str) -> List[str]:
        with open(path_to_file, "r", encoding="UTF-8") as f:
            lines: list[str] = [line.strip() for line in f]
        print("read {} lines from {}.".format(len(lines), path_to_file))
        return lines

    def __init__(self, filename: str, isTestFile: bool) -> None:
        if isTestFile:
            path_to_file = str(
                pathlib.Path(__file__).parents[2]
                / "tests"
                / "resources"
                / ("test-" + filename)
            )
        else:
            path_to_file = str(
                pathlib.Path(__file__).parents[2] / "resources" / filename
            )

        self.path_to_file: str = path_to_file
        self.input_lines: List[str] = self.read_input(path_to_file)
