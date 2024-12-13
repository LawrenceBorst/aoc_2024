from enum import IntEnum
from ..utils.data_loader import DataLoader
import numpy as np
from numpy.typing import NDArray


class Char(IntEnum):
    X = 1
    M = 2
    A = 3
    S = 4


Data = NDArray[np.int64]


class DataLoader04(DataLoader[Data]):
    def load(self) -> Data:
        data: list[list[Char]] = [
            [self._as_char(char) for char in self._remove_newline(line)]
            for line in self._data
        ]

        return np.asarray(data)

    def _remove_newline(self, line: str) -> str:
        return line.rstrip("\n")

    def _as_char(self, char: str) -> Char:
        if char == "X":
            return Char.X
        elif char == "M":
            return Char.M
        elif char == "A":
            return Char.A
        elif char == "S":
            return Char.S
        else:
            return ValueError('Char not in ["X", "M", "A", "S"]')
