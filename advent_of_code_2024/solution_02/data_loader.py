from ..utils.data_loader import DataLoader


Data = list[list[int]]


class DataLoader02(DataLoader[Data]):
    def load(self) -> Data:
        data: list[list[int]] = [
            [int(x) for x in self._remove_newline(line).split()] for line in self._data
        ]

        return data

    def _remove_newline(self, line: str) -> str:
        return line.rstrip("\n")
