import unittest
from typing import Dict, List

from aoc23.day11.cosmic_expansion import Galaxy, Universe
from aoc23.day11.solver import Day11Solver
from aoc23.utils.solver import compute_path_to_input_file


class TestUniverse(unittest.TestCase):
    def setUp(self) -> None:
        """is run before every test method"""
        self.solver: Day11Solver = Day11Solver(
            compute_path_to_input_file(__file__, "day11.txt")
        )
        self.universe: Universe = Universe.create(self.solver.input_lines)
        self.original_galaxies: List[Galaxy] = [
            Galaxy(1, 0, 3),
            Galaxy(2, 1, 7),
            Galaxy(3, 2, 0),
            Galaxy(4, 4, 6),
            Galaxy(5, 5, 1),
            Galaxy(6, 6, 9),
            Galaxy(7, 8, 7),
            Galaxy(8, 9, 0),
            Galaxy(9, 9, 4),
        ]
        self.expanded_galaxies: List[Galaxy] = [
            Galaxy(1, 0, 4),
            Galaxy(2, 1, 9),
            Galaxy(3, 2, 0),
            Galaxy(4, 5, 8),
            Galaxy(5, 6, 1),
            Galaxy(6, 7, 12),
            Galaxy(7, 10, 9),
            Galaxy(8, 11, 0),
            Galaxy(9, 11, 5),
        ]

    def tearDown(self) -> None:
        """is run after each test method"""
        pass

    def test_initialize_universe_with_galaxies(self) -> None:
        # for galaxy in self.universe.original_galaxies:
        #     print(f"original galaxy: {galaxy}")
        self.assertTrue(self.universe.original_galaxies == self.original_galaxies)

    def test_expand_universe(self) -> None:
        # for galaxy in self.universe.expanded_galaxies:
        #     print(f"expanded galaxy: {galaxy}")
        self.assertTrue(self.universe.expanded_galaxies == self.expanded_galaxies)

    def test_compute_shortest_path_identical_galaxy(self) -> None:
        galaxy1: Galaxy = self.universe.expanded_galaxies[0]
        self.assertTrue(galaxy1.shortest_distance(galaxy1) == 0)

    def get_expanded_galaxies(self, ids: List[int]) -> List[Galaxy]:
        galaxies: List[Galaxy] = []
        for id in ids:
            galaxy: Galaxy = list(
                filter(lambda g: g.id == id, self.universe.expanded_galaxies)
            )[0]
            galaxies.append(galaxy)
        return galaxies

    def test_compute_shortest_path_g5_to_g9(self) -> None:
        galaxies: List[Galaxy] = self.get_expanded_galaxies([5, 9])
        self.assertTrue(galaxies[0].shortest_distance(galaxies[1]) == 9)
        self.assertTrue(galaxies[1].shortest_distance(galaxies[0]) == 9)

    def test_compute_shortest_path_g1_to_g7(self) -> None:
        galaxies: List[Galaxy] = self.get_expanded_galaxies([1, 7])
        self.assertTrue(galaxies[0].shortest_distance(galaxies[1]) == 15)
        self.assertTrue(galaxies[1].shortest_distance(galaxies[0]) == 15)

    def test_compute_shortest_path_g3_to_g6(self) -> None:
        galaxies: List[Galaxy] = self.get_expanded_galaxies([3, 6])
        self.assertTrue(galaxies[0].shortest_distance(galaxies[1]) == 17)
        self.assertTrue(galaxies[1].shortest_distance(galaxies[0]) == 17)

    def test_compute_shortest_path_g8_to_g9(self) -> None:
        galaxies: List[Galaxy] = self.get_expanded_galaxies([8, 9])
        self.assertTrue(galaxies[0].shortest_distance(galaxies[1]) == 5)
        self.assertTrue(galaxies[1].shortest_distance(galaxies[0]) == 5)

    def test_compute_shortest_path_g7_to_g9(self) -> None:
        galaxies: List[Galaxy] = self.get_expanded_galaxies([7, 9])
        self.assertTrue(galaxies[0].shortest_distance(galaxies[1]) == 5)
        self.assertTrue(galaxies[1].shortest_distance(galaxies[0]) == 5)

    def test_task1(self) -> None:
        shortest_paths: List[Dict[str, int]] = self.universe.compute_shortest_paths()
        total_sum: int = sum(map(lambda x: x["dist"], shortest_paths))
        print(
            f"The sum of the lengths of the shortest path between every pair of galaxies amounts to {total_sum}."
        )
        # for dict in shortest_paths:
        #     print(dict)
        self.assertTrue(total_sum == 374)
