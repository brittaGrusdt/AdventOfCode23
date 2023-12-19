import re
from enum import Enum
from typing import Dict, List, ValuesView

CARD_STRENGTHS: Dict[str, int] = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


class CardType(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIRS = 3
    ONE_PAIR = 2
    HIGHEST_CARD = 1


class Hand:
    def __init__(self, line: str) -> None:
        values: List[str] = re.split("\\s", line)
        self.cards: str = values[0]
        self.bid: int = int(values[1])
        self.type: CardType = self.get_type()
        self.strengths: List[int] = self.get_strengths()

    def get_strengths(self) -> List[int]:
        strengths: List[int] = []
        for card in self.cards:
            strengths.append(CARD_STRENGTHS[card])
        return strengths

    def get_type(self) -> CardType:
        card_freq: Dict[str, int] = {}
        for card in self.cards:
            n: int = card_freq.get(card, 0)
            card_freq[card] = n + 1

        frequencies: ValuesView[int] = card_freq.values()
        if 5 in frequencies:
            card_type = CardType.FIVE_OF_A_KIND
        elif 4 in frequencies:
            card_type = CardType.FOUR_OF_A_KIND
        elif 3 in frequencies:
            if 2 in frequencies:
                card_type = CardType.FULL_HOUSE
            else:
                card_type = CardType.THREE_OF_A_KIND
        else:
            num_pairs: int = len(list(filter(lambda x: x == 2, frequencies)))
            match num_pairs:
                case 2:
                    card_type = CardType.TWO_PAIRS
                case 1:
                    card_type = CardType.ONE_PAIR
                case _:
                    card_type = CardType.HIGHEST_CARD

        return card_type
