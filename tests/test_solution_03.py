from advent_of_code_2024.solution_03.data_loader import DataLoader03
from advent_of_code_2024.solution_03.solution import Solution03
from unittest.mock import Mock
import pytest


def test_load(data_loader: DataLoader03):
    assert data_loader.load() == (
        ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
    )


def test_solution_1(solution: Solution03):
    assert solution.solution_1() == 161


@pytest.fixture
def solution(data_loader: DataLoader03) -> Solution03:
    return Solution03(data_loader)


@pytest.fixture
def data_loader(mocker: Mock, mock_data: list[str]) -> DataLoader03:
    mocker.patch(
        "advent_of_code_2024.utils.data_loader.DataLoader._read_data",
        return_value=mock_data,
    )

    return DataLoader03("some_path")


@pytest.fixture
def mock_data() -> list[str]:
    return ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))\n"]
