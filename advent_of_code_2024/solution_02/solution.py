from ..utils.solution import Solution
from .data_loader import Data


class Solution02(Solution[int, Data]):
    def __init__(self, data_loader):
        super().__init__(data_loader)

    def solution_1(self) -> int:
        safe_mask: list[bool] = [
            1 if self._has_conditions(report) else 0 for report in self._data
        ]

        return sum(safe_mask)

    def solution_2(self) -> int:
        return NotImplemented

    def _has_conditions(self, report: list[int]) -> bool:
        last_diff: int = 0

        for idx in range(len(report) - 1):
            diff: int = report[idx + 1] - report[idx]
            
            if abs(diff) == 0 or abs(diff) > 3:
                return False
            
            if (last_diff < 0 and diff > 0) or (last_diff > 0 and diff < 0):
                return False
            
            last_diff = diff

        return True
