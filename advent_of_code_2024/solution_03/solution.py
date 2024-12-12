from ..utils.solution import Solution
from .data_loader import Data
import re
from re import Match, Pattern
from typing import Annotated, Tuple


class Solution03(Solution[int, Data]):
    _pattern_1: Pattern

    def __init__(self, data_loader):
        super().__init__(data_loader)

        self._pattern_1 = re.compile(r"mul\(\d+,\d+\)")
        self._pattern_2 = re.compile(r"(mul\(\d+,\d+\))|don't|do")

    def solution_1(self) -> int:
        return sum(
            [
                sum([self._convert_op_to_num(x) for x in self._pattern_1.findall(line)])
                for line in self._data
            ]
        )

    def solution_2(self) -> int:
        do: bool = True
        sum: int = 0

        for line in self._data:
            for match in self._pattern_2.finditer(line):
                value, do = self._get_value(match, do)
                sum += value

        return sum

    def _get_value(self, match: Match, do: bool) -> Tuple[int, bool]:
        match_str: str = match.group(0)
        value: int = 0

        if match_str == "do":
            do = True
        elif match_str == "don't":
            do = False

        if do and match_str not in ["do", "don't"]:
            value = self._convert_op_to_num(match_str)

        return value, do

    def _convert_op_to_num(self, op: str) -> int:
        nums: Annotated[list[str], 2] = op[4:-1].split(",")

        return int(nums[0]) * int(nums[1])
