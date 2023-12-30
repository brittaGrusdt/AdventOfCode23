import pathlib
from abc import ABC, abstractmethod
from typing import List


def compute_path_to_input_file(path_to_calling_module: str) -> pathlib.Path:
    return pathlib.Path(path_to_calling_module).with_name("input.txt")


class Solver(ABC):
    """Class defining functions for reading input from text file"""

    @abstractmethod
    def run_task1(self) -> None:
        pass

    @abstractmethod
    def run_task2(self) -> None:
        pass

    def read_input(self, path_to_file: pathlib.Path) -> List[str]:
        with open(path_to_file, "r", encoding="UTF-8") as f:
            lines: list[str] = [line.strip() for line in f]
        print("read {} lines from {}.".format(len(lines), path_to_file))
        return lines

    def __init__(self, path_to_input_file: pathlib.Path) -> None:
        print(path_to_input_file)
        self.path_to_file: pathlib.Path = path_to_input_file
        self.input_lines: List[str] = self.read_input(self.path_to_file)
