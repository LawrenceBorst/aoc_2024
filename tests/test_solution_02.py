from advent_of_code_2024.solution_02.data_loader import DataLoader02
from advent_of_code_2024.solution_02.solution import Solution02
from unittest.mock import Mock
import pytest


def test_load(data_loader: DataLoader02):
    assert data_loader.load() == (
        [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9],
        ]
    )


def test_solution_1(solution: Solution02):
    assert solution.solution_1() == 2


@pytest.fixture
def solution(data_loader: DataLoader02) -> Solution02:
    return Solution02(data_loader)


@pytest.fixture
def data_loader(mocker: Mock, mock_data: list[str]) -> DataLoader02:
    mocker.patch(
        "advent_of_code_2024.utils.data_loader.DataLoader._read_data",
        return_value=mock_data,
    )

    return DataLoader02("some_path")


@pytest.fixture
def mock_data() -> list[str]:
    return [
        "7 6 4 2 1\n",
        "1 2 7 8 9\n",
        "9 7 6 2 1\n",
        "1 3 2 4 5\n",
        "8 6 4 4 1\n",
        "1 3 6 7 9\n",
    ]
