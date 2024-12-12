from pathlib import Path, PosixPath
from advent_of_code_2024.solution_03 import Solution03, DataLoader03


def main():
    base_path: PosixPath = Path(__file__).parent
    input_path = (
        base_path / "advent_of_code_2024" / "solution_03" / "input.txt"
    ).resolve()
    loader: DataLoader03 = DataLoader03(str(input_path))
    solution: Solution03 = Solution03(loader)

    print(solution.solution_1())


if __name__ == "__main__":
    main()
