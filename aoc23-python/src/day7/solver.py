from typing import List

from day7.camelcard import Hand
from utils.solver import Solver


class Day7Solver(Solver):
    def __init__(
        self, filename: str, isTestFile: bool, use_joker: bool = False
    ) -> None:
        super().__init__(filename, isTestFile)
        self.hands: List[Hand] = []
        for line in self.input_lines:
            hand = Hand(line, use_joker)
            self.hands.append(hand)
        self.sort_hands()

    @classmethod
    def create(cls, filename: str, isTestFile: bool, use_joker: bool) -> "Day7Solver":
        return cls(filename, isTestFile, use_joker)

    def sort_hands(self) -> None:
        self.hands.sort(key=lambda hand: (hand.type.value, hand.strengths))

    def compute_winnings(self) -> List[int]:
        ranks = range(1, len(self.hands) + 1)
        winnings: List[int] = [
            a * b for a, b in zip(ranks, list(map(lambda x: x.bid, self.hands)))
        ]
        return winnings

    def run_task1(self) -> None:
        # for hand in self.hands:
        #     print(
        #         f"{hand.cards}; type: {hand.type}; contains joker: {('J' in hand.cards and hand.use_joker)}"
        #     )
        winning: int = sum(self.compute_winnings())
        print(f"The total winnings are: {winning}")

    def run_task2(self) -> None:
        self.run_task1()
