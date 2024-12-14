from ..utils.data_loader import DataLoader
from typing import Tuple, Annotated


Coord = Annotated[Tuple[int, int], "(y, x)"]
Data = Tuple[list[Coord], Coord]


class DataLoader06(DataLoader[Data]):
    def load(self) -> Data:
        data: list[Coord] = []
        start: Coord

        lines: list[str] = [self._remove_newline(line) for line in self._data]

        for idx, line in enumerate(lines):
            data += [
                (idx, idx_char) for idx_char, char in enumerate(line) if char == "#"
            ]

            if (found_start := line.find("^")) != -1:
                start = (idx, found_start)

        return data, start

    def _remove_newline(self, line: str) -> str:
        return line.rstrip("\n")
