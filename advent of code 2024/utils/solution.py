from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from .data_loader import DataLoader

T = TypeVar("T")


class Solution(ABC, Generic[T]):
    _data: str

    def __init__(self, data_loader: DataLoader) -> None:
        self._data = data_loader.load()

    @abstractmethod
    def solution_1() -> T:
        return NotImplemented
    
    @abstractmethod
    def solution_2() -> T:
        return NotImplemented
