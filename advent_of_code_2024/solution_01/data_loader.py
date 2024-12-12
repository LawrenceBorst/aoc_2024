from typing import Tuple
from ..utils.data_loader import DataLoader
from typing import Annotated


Data = Tuple[list[int], list[int]]


class DataLoader01(DataLoader[Data]):
    def load(self) -> Data:
        """
        Loads the data for the two arrays
        """
        data: Annotated[list[int], 2] = [
            [int(x) for x in self._remove_newline(line).split()] for line in self._data
        ]
        col_1, col_2 = zip(*data)

        return list(col_1), list(col_2)

    def _remove_newline(self, line: str) -> str:
        return line.rstrip("\n")
