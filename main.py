from pathlib import Path, PosixPath
from advent_of_code_2024.solution_01 import Solution01, DataLoader01


def main():
    base_path: PosixPath = Path(__file__).parent
    input_path = (
        base_path / "advent_of_code_2024" / "solution_01" / "input.txt"
    ).resolve()
    loader: DataLoader01 = DataLoader01(str(input_path))
    solution: Solution01 = Solution01(loader)

    print(solution.solution_1())


if __name__ == "__main__":
    main()
