from advent_of_code_2024.solution_01.data_loader import DataLoader01
from advent_of_code_2024.solution_01.solution import Solution01
from unittest.mock import Mock
import pytest


def test_load(data_loader: DataLoader01):
    assert data_loader.load() == ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])


def test_solution_1(solution: Solution01):
    assert solution.solution_1() == 11


def test_solution_2(solution: Solution01):
    assert solution.solution_2() == 31


@pytest.fixture
def solution(data_loader: DataLoader01) -> Solution01:
    return Solution01(data_loader)


@pytest.fixture
def data_loader(mocker: Mock, mock_data: list[str]) -> DataLoader01:
    mocker.patch(
        "advent_of_code_2024.utils.data_loader.DataLoader._read_data",
        return_value=mock_data,
    )

    return DataLoader01("some_path")


@pytest.fixture
def mock_data() -> list[str]:
    return [
        "3   4\n",
        "4   3\n",
        "2   5\n",
        "1   3\n",
        "3   9\n",
        "3   3\n",
    ]
