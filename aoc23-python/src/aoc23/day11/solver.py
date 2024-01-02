from pathlib import Path
from typing import Dict, List

from aoc23.day11.cosmic_expansion import Universe
from aoc23.utils.solver import Solver


class Day11Solver(Solver):
    def __init__(
        self, path_to_input_file: Path, nb_replacement_empty_space: int = 2
    ) -> None:
        super().__init__(path_to_input_file)
        self.universe: Universe = Universe.create(
            self.input_lines, nb_replacement_empty_space
        )

    def run_task1(self) -> None:
        shortest_paths: List[Dict[str, int]] = self.universe.compute_shortest_paths()
        total_sum: int = sum(map(lambda x: x["dist"], shortest_paths))
        print(
            f"The sum of the lengths of the shortest path between every pair of galaxies amounts to {total_sum}."
        )

    def run_task2(self) -> None:
        self.universe: Universe = Universe.create(self.input_lines, 1000000)
        self.run_task1()
