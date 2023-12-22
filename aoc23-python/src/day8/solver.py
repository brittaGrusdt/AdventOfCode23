import itertools
import math
from typing import List, Tuple

from day8.haunted_wasteland import Network, Node
from utils.solver import Solver


class Day8Solver(Solver):
    def __init__(self, filename: str, isTestFile: bool) -> None:
        super().__init__(filename, isTestFile)
        self.network: Network = Network(self.input_lines)

    def get_next_nodes(self, current_nodes: List[str], num_iter: int) -> List[str]:
        len_cycle: int = len(self.network.directions)
        direction: str = self.network.directions[num_iter % len_cycle]
        moveTo: str = "left" if direction == "L" else "right"

        next_nodes: List[str] = []
        for current_node in current_nodes:
            node: Node = self.network.nodes[current_node]
            next_nodes.append(getattr(node, moveTo))

        return next_nodes

    def run_task1(self) -> None:
        zzz_reached: bool = False
        num_iter: int = 0
        next: str = "AAA"
        while not zzz_reached and num_iter <= 10000000:
            next = self.get_next_nodes([next], num_iter)[0]
            num_iter += 1
            zzz_reached = next == "ZZZ"

        print(f"number iterations: {num_iter}, zzz reached: {zzz_reached}")

        # def run_task2(self) -> None:
        #     """straight forward implementation, same logic as for task1 (slow)"""
        #     num_iter: int = 0
        #     next_nodes: List[str] = list(
        #         filter(lambda name: name.endswith("A"), self.network.nodes.keys())
        #     )
        #     all_end_with_z: bool = all(map(lambda x: x.endswith("Z"), next_nodes))
        #     while not all_end_with_z and num_iter <= 1000000000:
        #         next_nodes = self.get_next_nodes(next_nodes, num_iter)
        #         num_iter += 1
        #         all_end_with_z = all(map(lambda x: x.endswith("Z"), next_nodes))

        #     print(f"number iterations: {num_iter}, zzz reached: {all_end_with_z}")

    def find_least_commmon_multiple(self, iterations: List[List[int]]) -> float:
        combinations: List[Tuple[int]] = list(itertools.product(*iterations))
        least_common_multiple: float = math.inf
        for combi in combinations:
            lcm: float = math.lcm(*combi)
            if lcm < least_common_multiple:
                least_common_multiple = lcm
        return least_common_multiple

    def run_task2(self) -> None:
        next_nodes: List[str] = list(
            filter(lambda name: name.endswith("A"), self.network.nodes.keys())
        )
        len_cycle: int = len(self.network.directions)

        successful_iterations: List[List[int]] = []
        for current_node in next_nodes:
            num_iter: int = 0
            cycle_completed: bool = False
            moves: List[str] = []
            iterations: List[int] = []
            next_node = current_node
            while not cycle_completed and num_iter < 1000000000:
                next_node: str = self.get_next_nodes([next_node], num_iter)[0]
                idx: int = num_iter % len_cycle
                direction = self.network.directions[idx]
                move: str = direction + next_node + str(idx)
                num_iter += 1
                if move in moves:
                    cycle_completed = True
                else:
                    moves.append(move)

                if next_node.endswith("Z") and not cycle_completed:
                    iterations.append(num_iter)

            if len(iterations) > 0:
                successful_iterations.append(iterations)

        print(f"successful iterations: {successful_iterations}")
        least_common_multiple: float = self.find_least_commmon_multiple(
            successful_iterations
        )
        print(f"nb iterations needed for all to end with Z: {least_common_multiple}")
