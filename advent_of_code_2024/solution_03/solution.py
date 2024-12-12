from ..utils.solution import Solution
from .data_loader import Data
import re
from re import Pattern
from typing import Annotated


class Solution03(Solution[int, Data]):
    _pattern: Pattern

    def __init__(self, data_loader):
        super().__init__(data_loader)

        self._pattern = re.compile(r"mul\(\d+,\d+\)")

    def solution_1(self) -> int:
        return sum(
            [
                sum([self._convert_op_to_num(x) for x in self._pattern.findall(line)])
                for line in self._data
            ]
        )

    def solution_2(self) -> int:
        return NotImplemented

    def _convert_op_to_num(self, op: str) -> int:
        nums: Annotated[list[str], 2] = op[4:-1].split(",")

        return int(nums[0]) * int(nums[1])
