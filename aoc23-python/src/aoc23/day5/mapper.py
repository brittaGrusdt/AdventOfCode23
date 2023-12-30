import re
from typing import Dict, List, TypeAlias

MapperType: TypeAlias = Dict[str, int]


class Mapper:
    """"""

    def __init__(self, categories: List[str], mappings: List[MapperType]) -> None:
        self.source_cat: str = categories[0].strip()
        self.target_cat: str = categories[1].strip()
        self.mappings: List[MapperType] = mappings

    @classmethod
    def create(cls, input: List[str]) -> "Mapper":
        """creates an instance of class Mapper, first input line equals 'x-to-y map:' where x is source and y target.
        The following lines each consist of 3 numbers, the destination start, the source start and the length."""
        name: str = re.split("\\s+", input[0])[0].strip()
        categories: List[str] = name.split("-to-")

        # process mappings
        mappings: List[MapperType] = []
        for line in input[1:]:
            map_values: list[str] = re.split("\\s+", line)
            map_dict: dict[str, int] = {
                "src": int(map_values[1]),
                "dest": int(map_values[0]),
                "length": int(map_values[2]),
            }
            mappings.append(map_dict)
        return cls(categories, mappings)

    def do_mapping(self, num: int) -> int:
        """computes for given number (num) the mapping as defined by this Mapper.
        If num is not contained in any range to map, it is 'mapped' to itself and simply returned."""
        mappings = list(
            filter(
                lambda map: num >= map["src"] and num <= map["src"] + map["length"] - 1,
                self.mappings,
            )
        )
        num_elem: int = len(mappings)
        if num_elem > 1:
            raise ValueError(
                f"illegal state: {num} should only be contained in one range of mapping!"
            )
        if num_elem == 0:
            mapped_value = num
        else:
            delta = num - mappings[0]["src"]
            mapped_value = mappings[0]["dest"] + delta

        return mapped_value

    def reverse_mappings(self) -> None:
        src_cat: str = self.source_cat
        self.source_cat = self.target_cat
        self.target_cat: str = src_cat

        for mapping in self.mappings:
            src: int = mapping["src"]
            mapping["src"] = mapping["dest"]
            mapping["dest"] = src
