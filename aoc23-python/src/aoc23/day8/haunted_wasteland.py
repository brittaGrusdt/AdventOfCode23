import re
from typing import Dict, List, NamedTuple


class Node(NamedTuple):
    name: str
    left: str
    right: str


class Network:
    def __init__(self, input_lines: List[str]) -> None:
        self.directions: str = input_lines[0]
        self.nodes: Dict[str, Node] = {}

        for line in input_lines[1:]:
            if line == "":
                continue
            components: List[str] = re.split("=", line)
            name: str = components[0].strip()

            pattern: re.Pattern[str] = re.compile("\\([A-Z1-9]{3}, [A-Z1-9]{3}\\)")
            matched = pattern.match(components[1].strip())
            if matched is None:
                raise ValueError(f"{components[1]} does not match pattern {pattern}!")
            nodes: List[str] = re.split(",", matched.group())
            left: str = nodes[0][1:].strip()
            right: str = nodes[1][:-1].strip()
            self.nodes[name] = Node(name, left, right)
        print(f"Network build. Number direction instructions: {len(self.directions)}")
