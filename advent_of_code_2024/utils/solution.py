from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from .data_loader import DataLoader

T = TypeVar("T")
U = TypeVar("U")


class Solution(ABC, Generic[T, U]):
    _data: U

    def __init__(self, data_loader: DataLoader[U]) -> None:
        self._data = data_loader.load()

    @abstractmethod
    def solution_1(self) -> T:
        return NotImplemented
    
    @abstractmethod
    def solution_2(self) -> T:
        return NotImplemented
