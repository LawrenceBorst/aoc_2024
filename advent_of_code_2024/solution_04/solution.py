from ..utils.solution import Solution
from .data_loader import Data, Char
import numpy as np
from numpy.typing import NDArray


class Solution04(Solution[int, Data]):
    def __init__(self, data_loader):
        super().__init__(data_loader)

    def solution_1(self) -> int:
        height, width = self._data.shape
        count: int = 0

        for y in range(0, height):
            padding_y = max(0, y - height + 4)
            for x in range(0, width):
                arr = self._data[y : y + 4, x : x + 4]

                # Pad to not miss out the corners
                padding_x = max(0, x - width + 4)
                arr = np.pad(arr, pad_width=((0, padding_y), (0, padding_x)))

                count += self._scan_4_by_4(arr)

        return count

    def solution_2(self) -> int:
        height, width = self._data.shape
        count: int = 0

        for y in range(0, height):
            padding_y = max(0, y - height + 3)
            for x in range(0, width):
                arr = self._data[y : y + 3, x : x + 3]

                # Pad to not miss out the corners
                padding_x = max(0, x - width + 3)
                arr = np.pad(arr, pad_width=((0, padding_y), (0, padding_x)))

                count += self._scan_3_by_3(arr)

        return count

    def _scan_4_by_4(self, arr: NDArray[np.int64]) -> int:
        """
        Returns the number of hits in a 4 by 4 grid for the word "xmas"
        For the row, column and diagonal intersecting at (0, 0)
        """
        count: int = 0
        xmas: np.ndarray[np.int64] = np.asarray([Char.X, Char.M, Char.A, Char.S])

        if np.array_equal(arr[0, :], xmas):
            count += 1

        if np.array_equal(arr[0, ::-1], xmas):
            count += 1

        if np.array_equal(arr[:, 0], xmas):
            count += 1

        if np.array_equal(arr[::-1, 0], xmas):
            count += 1

        if np.array_equal(arr.diagonal(), xmas):
            count += 1

        if np.array_equal(arr.diagonal()[::-1], xmas):
            count += 1

        if np.array_equal(np.flipud(arr).diagonal(), xmas):
            count += 1

        if np.array_equal(np.flipud(arr).diagonal()[::-1], xmas):
            count += 1

        return count

    def _scan_3_by_3(self, arr: NDArray[np.int64]) -> int:
        """
        Returns the number of hits in a 3 by 3 grid for the word "mas" in an x-shape
        """
        hits: int = 0
        xmas: np.ndarray[np.int64] = np.asarray([Char.M, Char.A, Char.S])

        if np.array_equal(arr.diagonal(), xmas):
            hits += 1

        if np.array_equal(arr.diagonal()[::-1], xmas):
            hits += 1

        if np.array_equal(np.flipud(arr).diagonal(), xmas):
            hits += 1

        if np.array_equal(np.flipud(arr).diagonal()[::-1], xmas):
            hits += 1

        if hits == 2:
            return 1

        return 0
