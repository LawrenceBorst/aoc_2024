from ..utils.data_loader import DataLoader


Data = list[str]


class DataLoader03(DataLoader[Data]):
    def load(self) -> Data:
        """
        Loads the data for the two arrays
        """
        data: list[str] = [self._remove_newline(line) for line in self._data]

        return data

    def _remove_newline(self, line: str) -> str:
        return line.rstrip("\n")
