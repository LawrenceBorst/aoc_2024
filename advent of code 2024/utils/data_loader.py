from io import TextIOWrapper
from typing import TypeVar, Generic
from abc import ABC, abstractmethod

U = TypeVar("U")


class DataLoader(ABC, Generic[U]):
    _data: str

    def __init__(self, path: str) -> None:
        self._data = self._read_data(path)

    def _read_data(self, path: str) -> list[str]:
        file: TextIOWrapper = open(path, "r")
        return file.readlines()

    @abstractmethod
    def load(self) -> U:
        return NotImplemented
