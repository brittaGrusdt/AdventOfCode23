import pathlib
from abc import ABC, abstractmethod
from typing import List


def compute_path_to_input_file(
    path_to_calling_module: str, name_test_file: str = ""
) -> pathlib.Path:
    if name_test_file != "":
        computed_path: pathlib.Path = (
            pathlib.Path(path_to_calling_module).parent / "resources" / name_test_file
        )
    else:
        # path_to_calling_module should be __main__.py, with_name replaces the final path component!
        computed_path: pathlib.Path = pathlib.Path(path_to_calling_module).with_name(
            "input.txt"
        )
    return computed_path


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
        self.path_to_file: pathlib.Path = path_to_input_file
        self.input_lines: List[str] = self.read_input(self.path_to_file)
