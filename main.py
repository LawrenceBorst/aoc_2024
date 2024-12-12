from pathlib import Path, PosixPath
from advent_of_code_2024.solution_02 import Solution02, DataLoader02


def main():
    base_path: PosixPath = Path(__file__).parent
    input_path = (
        base_path / "advent_of_code_2024" / "solution_02" / "input.txt"
    ).resolve()
    loader: DataLoader02 = DataLoader02(str(input_path))
    solution: Solution02 = Solution02(loader)

    print(solution.solution_1())


if __name__ == "__main__":
    main()
