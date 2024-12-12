from ..utils.solution import Solution
from .data_loader import Data
from typing import Annotated
from collections import Counter


class Solution01(Solution[int, Data]):
    def __init__(self, data_loader):
        super().__init__(data_loader)

    def solution_1(self) -> int:
        col_1, col_2 = self._data

        col_1.sort()
        col_2.sort()

        unzipped_sorted_data: Annotated[list[int], 2] = list(zip(col_1, col_2))

        return sum([abs(x[0] - x[1]) for x in unzipped_sorted_data])

    def solution_2(self) -> int:
        col_1, col_2 = self._data

        counts: Counter = Counter(col_2)

        return sum([x * counts[x] for x in col_1])
