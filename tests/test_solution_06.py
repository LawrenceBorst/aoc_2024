from advent_of_code_2024.solution_06.data_loader import DataLoader06
from advent_of_code_2024.solution_06.solution import Solution06
from unittest.mock import Mock
import pytest


def test_load(data_loader: DataLoader06):
    assert data_loader.load() == (
        [(0, 4), (1, 9), (3, 2), (4, 7), (6, 1), (7, 8), (8, 0), (9, 6)],
        (6, 4),
    )


def test_solution_1(solution: Solution06):
    assert solution.solution_1() == 41


@pytest.fixture
def solution(data_loader: DataLoader06) -> Solution06:
    return Solution06(data_loader)


@pytest.fixture
def data_loader(mocker: Mock, mock_data: list[str]) -> DataLoader06:
    mocker.patch(
        "advent_of_code_2024.utils.data_loader.DataLoader._read_data",
        return_value=mock_data,
    )

    return DataLoader06("some_path")


@pytest.fixture
def mock_data() -> list[str]:
    return [
        "....#.....\n",
        ".........#\n",
        "..........\n",
        "..#.......\n",
        ".......#..\n",
        "..........\n",
        ".#..^.....\n",
        "........#.\n",
        "#.........\n",
        "......#...",
    ]
