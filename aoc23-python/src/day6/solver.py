import math
import re
from typing import List, Sequence, Tuple

from utils.solver import Solver


class Day6Solver(Solver):
    def __init__(self, filename: str, isTestFile: bool) -> None:
        super().__init__(filename, isTestFile)
        durations: List[int] = list(map(int, re.split("\\s+", self.input_lines[0])[1:]))
        min_distances: List[int] = list(
            map(int, re.split("\\s+", self.input_lines[1])[1:])
        )
        self.data: List[Tuple[int, int]] = list(zip(durations, min_distances))

    def get_travelled_dist(self, duration: int, ms_hold: int) -> int:
        return (duration - ms_hold) * ms_hold

    def get_ms_for_given_dist(self, time: int, dist_travelled: int) -> Tuple[int, int]:
        a: int = -1
        b: int = time
        c: int = -dist_travelled
        x_zero1: float = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        x_zero2: float = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        if x_zero1 < x_zero2:
            result: Tuple[int, int] = (math.ceil(x_zero1), math.floor(x_zero2))
        else:
            result: Tuple[int, int] = (math.ceil(x_zero2), math.floor(x_zero1))

        return result

    def compute_range_ms_to_hold(self, time: int, dist: int) -> Sequence[int]:
        ms_hold: int = 1
        travelled: int = time - 1
        while travelled <= dist and ms_hold < time:
            travelled = self.get_travelled_dist(time, ms_hold)
            ms_hold += 1

        if ms_hold == time:
            raise ValueError(
                f"this record cannot be done faster than the record. Duration: {time}, record: {dist}"
            )
        result: Tuple[int, int] = self.get_ms_for_given_dist(time, travelled)
        return result

    def run_task1(self) -> None:
        num_solutions: int = 1
        for time, dist in self.data:
            interval: Sequence[int] = self.compute_range_ms_to_hold(time, dist)
            num_solutions *= interval[1] - interval[0] + 1
        print(f"In total there are {num_solutions} possibilities.")

    def run_task2(self) -> None:
        time: int = int("".join([str(x) for x in list(zip(*self.data))[0]]))
        distance: int = int("".join([str(x) for x in list(zip(*self.data))[1]]))
        self.data = [(time, distance)]
        self.run_task1()
