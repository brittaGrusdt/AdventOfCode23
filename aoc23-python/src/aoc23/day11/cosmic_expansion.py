import copy
from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class Galaxy:
    id: int
    row: int
    col: int

    def shortest_distance(self, other: "Galaxy") -> int:
        dist_rows: int = self.row - other.row
        dist_cols: int = self.col - other.col
        dist_rows = dist_rows * -1 if dist_rows < 0 else dist_rows
        dist_cols = dist_cols * -1 if dist_cols < 0 else dist_cols
        return dist_rows + dist_cols


class Universe:
    def __init__(
        self,
        galaxies: List[Galaxy],
        nb_rows: int,
        nb_cols: int,
        expand_by: int,
    ) -> None:
        # initialize original universe
        self.original_nb_rows: int = nb_rows
        self.original_nb_cols: int = nb_cols
        self.original_galaxies: List[Galaxy] = sorted(
            galaxies, key=lambda g: (g.row, g.col)
        )
        # initialize expanded universe
        self.expanded_galaxies: List[Galaxy] = copy.deepcopy(self.original_galaxies)
        (nb_added_rows, nb_added_cols) = self.expand(expand_by)
        self.expanded_nb_rows: int = nb_rows + nb_added_rows
        self.expanded_nb_cols: int = nb_cols + nb_added_cols
        self.expaneded_galaxies: List[Galaxy] = sorted(
            self.expanded_galaxies, key=lambda g: (g.row, g.col)
        )

    @classmethod
    def create(cls, input_lines: List[str], expand_by: int = 2) -> "Universe":
        galaxies: List[Galaxy] = []
        for idx_row, line in enumerate(input_lines):
            num_occ: int = line.count("#")
            search_from_idx: int = 0
            for _ in range(1, num_occ + 1):
                idx_col: int = line.index("#", search_from_idx)
                galaxy: Galaxy = Galaxy(len(galaxies) + 1, idx_row, idx_col)
                search_from_idx = idx_col + 1
                galaxies.append(galaxy)
        return cls(galaxies, len(input_lines), len(input_lines[0]), expand_by)

    def __update_rows_columns(
        self, indices_no_galaxies: List[int], axis: int, num_added_empty_lines: int
    ) -> int:
        """updates the indices of the galaxies of this universe. Rows/Columns without galaxies count as twice as big.
        axis=1 refers to rows, axis=0 refers to columns."""
        num_added: int = 0
        for idx in sorted(indices_no_galaxies):
            #  use original indices for comparison
            if axis == 1:
                original_galaxies = list(
                    filter(lambda g: g.row > idx, self.original_galaxies)
                )
            elif axis == 0:
                original_galaxies = list(
                    filter(lambda g: g.col > idx, self.original_galaxies)
                )
            else:
                raise ValueError(
                    f"Axis must be equal to 0 or 1, but found to be: {axis}."
                )
            # update galaxies in expanded_galaxies list!
            galaxies = list(
                filter(
                    lambda g: g.id in map(lambda x: x.id, original_galaxies),
                    self.expanded_galaxies,
                )
            )
            for galaxy in galaxies:
                if axis == 1:
                    galaxy.row += num_added_empty_lines
                else:
                    galaxy.col += num_added_empty_lines
            num_added += 1
        return num_added

    def expand(self, expand_by: int) -> Tuple[int, int]:
        rows_with_galaxies: List[int] = list(
            map(lambda galaxy: galaxy.row, self.original_galaxies)
        )
        cols_with_galaxies: List[int] = list(
            map(lambda galaxy: galaxy.col, self.original_galaxies)
        )

        rows_no_galaxies: List[int] = [
            row for row in range(self.original_nb_rows) if row not in rows_with_galaxies
        ]

        cols_no_galaxies: List[int] = [
            col for col in range(self.original_nb_cols) if col not in cols_with_galaxies
        ]

        num_added_rows: int = self.__update_rows_columns(
            rows_no_galaxies, 1, expand_by - 1
        )
        num_added_cols: int = self.__update_rows_columns(
            cols_no_galaxies, 0, expand_by - 1
        )
        return (num_added_rows, num_added_cols)

    def compute_shortest_paths(self) -> List[Dict[str, int]]:
        shortest_paths: List[Dict[str, int]] = []
        for idx1, galaxy1 in enumerate(self.expanded_galaxies[:-1]):
            for galaxy2 in self.expanded_galaxies[idx1 + 1 :]:
                dist: int = galaxy1.shortest_distance(galaxy2)
                shortest_paths.append(
                    {"id1": galaxy1.id, "id2": galaxy2.id, "dist": dist}
                )

        return shortest_paths
