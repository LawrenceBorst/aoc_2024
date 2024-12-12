from advent_of_code_2024.solution_03.data_loader import DataLoader03
from advent_of_code_2024.solution_03.solution import Solution03
from unittest.mock import Mock


def test_load(mocker: Mock):
    mock_data: list[str] = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))\n"]

    mocker.patch(
        "advent_of_code_2024.utils.data_loader.DataLoader._read_data",
        return_value=mock_data,
    )

    data_loader: DataLoader03 = DataLoader03("some_path")

    assert data_loader.load() == (
        ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
    )


def test_solution_1(mocker: Mock):
    mock_data: list[str] = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))\n"]

    mocker.patch(
        "advent_of_code_2024.utils.data_loader.DataLoader._read_data",
        return_value=mock_data,
    )

    dataloader: DataLoader03 = DataLoader03("some_path")
    solution: Solution03 = Solution03(dataloader)
    
    assert solution.solution_1() == 161


def test_solution_2(mocker: Mock):
    mock_data: list[str] = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))\n"]

    mocker.patch(
        "advent_of_code_2024.utils.data_loader.DataLoader._read_data",
        return_value=mock_data,
    )

    dataloader: DataLoader03 = DataLoader03("some_path")
    solution: Solution03 = Solution03(dataloader)

    assert solution.solution_2() == 48
