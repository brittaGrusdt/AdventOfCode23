import pathlib
import re
from typing import List, Sequence

import numpy as np
from utils.solver import Solver

from day5.mapper import Mapper


class Day5Solver(Solver):
    def __init__(self, filename: str, absolute_path: str = "") -> None:
        if not absolute_path:
            absolute_path = str(
                pathlib.Path(__file__).parents[2] / "resources" / filename
            )
        super().__init__(absolute_path)
        digits: list[int] = list(map(int, re.findall(r"\d+", self.input_lines[0])))

        self.seeds: Sequence[int] = digits
        self.mappers: List[Mapper] = self.create_mappers()

    def create_mappers(self) -> List[Mapper]:
        num_lines: int = len(self.input_lines)
        mappers: List[Mapper] = []
        start: int = 2
        end: int = 4
        while end <= num_lines:
            if end == num_lines:
                contents: List[str] = self.input_lines[start : end + 1]
                mappers.append(Mapper.create(contents))
                end += 1

            elif len(self.input_lines[end]) == 0:
                contents: List[str] = self.input_lines[start:end]
                mappers.append(Mapper.create(contents))
                start = end + 1
                end += 1

            else:
                end += 1
        return mappers

    def remove_overlap(self, seed_ranges: List[Sequence[int]]) -> List[Sequence[int]]:
        sorted_ranges: List[Sequence[int]] = sorted(seed_ranges, key=lambda r: r[0])
        updated_ranges: List[Sequence[int]] = []

        idx: int = 0
        while idx < len(sorted_ranges):
            current_range: Sequence[int] = sorted_ranges[idx]
            if idx == len(sorted_ranges) - 1:
                updated_ranges.append(current_range)
                break
            next_range: Sequence[int] = sorted_ranges[idx + 1]

            if current_range[-1] > next_range[0]:
                if next_range[-1] >= current_range[-1]:
                    end: int = next_range[-1] + 1  # end is exclusive
                else:
                    end = current_range[-1]
                idx += 1  # skip next range
                updated_ranges.append(range(current_range[0], end))
            else:
                updated_ranges.append(current_range)
            idx += 1

        return updated_ranges

    def compute_seeds_from_ranges(self, numbers: Sequence[int]) -> List[Sequence[int]]:
        start_indices = np.asarray(numbers[0::2])
        len_ranges = np.asarray(numbers[1::2])
        end_indices = start_indices + len_ranges
        seed_ranges: List[Sequence[int]] = list(
            map(lambda t: range(t[0], t[1]), list(zip(start_indices, end_indices)))
        )
        sorted_ranges: List[Sequence[int]] = sorted(seed_ranges, key=lambda r: r[0])
        # updated_ranges: List[Sequence[int]] = self.remove_overlap(seed_ranges)
        # print(
        #     f"#original ranges: {len(seed_ranges)} #updated ranges: {len(updated_ranges)}"
        # )
        # print(sorted(seed_ranges, key=lambda r: r[0]))
        # print(updated_ranges)
        return sorted_ranges

    def compute_location_nums(
        self, first_cat: str = "seed", last_cat: str = "location"
    ) -> List[int]:
        location_nums: List[int] = []
        for seed in self.seeds:
            cat = first_cat
            mapped_value: int = seed
            while cat != last_cat:
                mappers: List[Mapper] = list(
                    filter(lambda mapper: mapper.source_cat == cat, self.mappers)
                )
                if len(mappers) == 0:
                    raise ValueError(
                        f"illegal state: there can only be one mapping with key {cat}!"
                    )
                cat: str = mappers[0].target_cat
                mapped_value: int = mappers[0].do_mapping(mapped_value)
            location_nums.append(mapped_value)
        return location_nums

    def run_task1(self) -> None:
        location_nums: List[int] = self.compute_location_nums()
        print(f"lowest location number is {min(location_nums)}")

    def isInSeedRange(self, x: int, ranges: List[Sequence[int]]) -> bool:
        found: bool = False
        for seed_range in ranges:
            start: int = seed_range[0]
            end: int = seed_range[-1]
            if x >= start and x <= end:
                found = True
            if x < start or found:
                break
        return found

    def run_task2(self) -> None:
        digits: List[Sequence[int]] = self.compute_seeds_from_ranges(self.seeds)
        num: int = 1
        lowest_location_num: float = float("Inf")
        for seq in digits:
            print(f"compute range num: {num}")
            self.seeds = seq
            location_nums: Sequence[int] = self.compute_location_nums()
            lowest: int = min(location_nums)
            if lowest < lowest_location_num:
                lowest_location_num = lowest
            num += 1

        print(f"lowest location number is {lowest_location_num}")

    def run_task2_reversed(self) -> None:
        digits: List[Sequence[int]] = self.compute_seeds_from_ranges(self.seeds)
        # The reverse version did NOT yield the right answer!  And is also too slow!
        for mapper in self.mappers:
            mapper.reverse_mappings()

        # self.seeds = [137516820]
        # result: int = self.compute_location_nums("location", "seed")[0]
        # print(f"corresponding seed: {result}")

        value: int = 0
        location_num: int = 0  # 137516820
        self.seeds = [location_num]
        found: bool = False
        stop_at: int = 10000000000
        while not found and location_num <= stop_at:
            if location_num % 1000000 == 0:
                print(f"{location_num} done...")
            value = self.compute_location_nums("location", "seed")[0]
            found = self.isInSeedRange(value, digits)
            location_num += 1
            self.seeds[0] = location_num

        if found:
            print(f"lowest location number should be {location_num-1}")
            for mapper in self.mappers:
                mapper.reverse_mappings()

            self.seeds = [value]
            result: int = self.compute_location_nums()[0]
            print(f"lowest location number is {result}")
        else:
            print(f"Noting found abfter {stop_at} location nummbers were tested.")
