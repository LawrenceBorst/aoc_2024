from advent_of_code_2024.solution_04.data_loader import DataLoader04, Char
from advent_of_code_2024.solution_04.solution import Solution04
from unittest.mock import Mock
import pytest
import numpy as np


def test_load(data_loader: DataLoader04):
    assert np.array_equal(
        data_loader.load(),
        np.asarray(
            [
                [
                    Char.M,
                    Char.M,
                    Char.M,
                    Char.S,
                    Char.X,
                    Char.X,
                    Char.M,
                    Char.A,
                    Char.S,
                    Char.M,
                ],
                [
                    Char.M,
                    Char.S,
                    Char.A,
                    Char.M,
                    Char.X,
                    Char.M,
                    Char.S,
                    Char.M,
                    Char.S,
                    Char.A,
                ],
                [
                    Char.A,
                    Char.M,
                    Char.X,
                    Char.S,
                    Char.X,
                    Char.M,
                    Char.A,
                    Char.A,
                    Char.M,
                    Char.M,
                ],
                [
                    Char.M,
                    Char.S,
                    Char.A,
                    Char.M,
                    Char.A,
                    Char.S,
                    Char.M,
                    Char.S,
                    Char.M,
                    Char.X,
                ],
                [
                    Char.X,
                    Char.M,
                    Char.A,
                    Char.S,
                    Char.A,
                    Char.M,
                    Char.X,
                    Char.A,
                    Char.M,
                    Char.M,
                ],
                [
                    Char.X,
                    Char.X,
                    Char.A,
                    Char.M,
                    Char.M,
                    Char.X,
                    Char.X,
                    Char.A,
                    Char.M,
                    Char.A,
                ],
                [
                    Char.S,
                    Char.M,
                    Char.S,
                    Char.M,
                    Char.S,
                    Char.A,
                    Char.S,
                    Char.X,
                    Char.S,
                    Char.S,
                ],
                [
                    Char.S,
                    Char.A,
                    Char.X,
                    Char.A,
                    Char.M,
                    Char.A,
                    Char.S,
                    Char.A,
                    Char.A,
                    Char.A,
                ],
                [
                    Char.M,
                    Char.A,
                    Char.M,
                    Char.M,
                    Char.M,
                    Char.X,
                    Char.M,
                    Char.M,
                    Char.M,
                    Char.M,
                ],
                [
                    Char.M,
                    Char.X,
                    Char.M,
                    Char.X,
                    Char.A,
                    Char.X,
                    Char.M,
                    Char.A,
                    Char.S,
                    Char.X,
                ],
            ]
        ),
    )


def test_solution_1(solution: Solution04):
    assert solution.solution_1() == 18


def test_solution_2(solution: Solution04):
    assert solution.solution_2() == 31


@pytest.fixture
def solution(data_loader: DataLoader04) -> Solution04:
    return Solution04(data_loader)


@pytest.fixture
def data_loader(mocker: Mock, mock_data: list[str]) -> DataLoader04:
    mocker.patch(
        "advent_of_code_2024.utils.data_loader.DataLoader._read_data",
        return_value=mock_data,
    )

    return DataLoader04("some_path")


@pytest.fixture
def mock_data() -> list[str]:
    return [
        "MMMSXXMASM\n",
        "MSAMXMSMSA\n",
        "AMXSXMAAMM\n",
        "MSAMASMSMX\n",
        "XMASAMXAMM\n",
        "XXAMMXXAMA\n",
        "SMSMSASXSS\n",
        "SAXAMASAAA\n",
        "MAMMMXMMMM\n",
        "MXMXAXMASX",
    ]
