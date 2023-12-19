import re
from enum import Enum
from typing import Dict, KeysView, List, ValuesView

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
    def __init__(self, line: str, use_joker: bool = False) -> None:
        self.use_joker: bool = use_joker
        values: List[str] = re.split("\\s", line)
        self.cards: str = values[0]
        self.bid: int = int(values[1])
        self.type: CardType = self.get_type()
        self.strengths: List[int] = self.get_strengths()

    def get_strengths(self) -> List[int]:
        strengths: List[int] = []
        for card in self.cards:
            if self.use_joker and card == "J":
                strengths.append(1)
            else:
                strengths.append(CARD_STRENGTHS[card])
        return strengths

    def get_type(self) -> CardType:
        card_freq: Dict[str, int] = {}
        for card in self.cards:
            n: int = card_freq.get(card, 0)
            card_freq[card] = n + 1

        frequencies: ValuesView[int] = card_freq.values()
        cards: KeysView[str] = card_freq.keys()
        num_jokers: int = card_freq.get("J", 0)

        if 5 in frequencies:
            card_type = CardType.FIVE_OF_A_KIND
        elif 4 in frequencies:
            card_type = CardType.FOUR_OF_A_KIND
            # 4 of a kind + 1 joker -> 5 of a kind
            if self.use_joker and num_jokers in [4, 1]:
                card_type = CardType.FIVE_OF_A_KIND

        elif 3 in frequencies:
            if 2 in frequencies:
                card_type = CardType.FULL_HOUSE
                # 2 or 3 Jokers -> 5 of a kind
                if self.use_joker and num_jokers in [2, 3]:
                    card_type = CardType.FIVE_OF_A_KIND
            else:
                card_type = CardType.THREE_OF_A_KIND
                if self.use_joker:
                    if num_jokers in [3, 1]:
                        card_type = CardType.FOUR_OF_A_KIND
        else:
            num_pairs: int = len(list(filter(lambda x: x == 2, frequencies)))
            match num_pairs:
                case 2:
                    card_type = CardType.TWO_PAIRS
                    if self.use_joker:
                        if num_jokers == 2:  # e.g. JJAA3
                            card_type = CardType.FOUR_OF_A_KIND
                        elif num_jokers == 1:  # e.g., TTKKJ
                            card_type = CardType.FULL_HOUSE
                case 1:
                    card_type = CardType.ONE_PAIR
                    if self.use_joker:
                        if num_jokers in [1, 2]:  # e.g., JJA23 or AAJ23
                            card_type = CardType.THREE_OF_A_KIND
                case _:
                    card_type = CardType.HIGHEST_CARD
                    if self.use_joker and "J" in cards:  # e.g., AJT23
                        card_type = CardType.ONE_PAIR

        return card_type
