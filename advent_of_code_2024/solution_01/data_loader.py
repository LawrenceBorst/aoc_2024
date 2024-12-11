from ..utils.data_loader import DataLoader
from typing import Tuple, List


Data = Tuple[List[int], List[int]]


class DataLoader01(DataLoader[Data]):
    def load(self) -> Data:
        return [], []
