from pathlib import Path, PosixPath
from advent_of_code_2024.utils import Solution, DataLoader
import importlib
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Gets solutions to the AOC problems")
    parser.add_argument("problem", type=int, help="the number of the problem")

    args = parser.parse_args()

    if not validate_args(args):
        raise Exception("Problem argument not in the range 1 to 25 inclusive")

    run(args.problem)


def validate_args(args) -> bool:
    problem: int = args.problem

    if problem <= 0 or problem > 25:
        return False

    return True


def run(problem: int) -> None:
    base_path: PosixPath = Path(__file__).parent

    sol_str: str = str(problem).zfill(2)
    class_module = importlib.import_module(f"advent_of_code_2024.solution_{sol_str}")

    input_path = (
        base_path / "advent_of_code_2024" / f"solution_{sol_str}" / "input.txt"
    ).resolve()

    loader: DataLoader = getattr(class_module, f"DataLoader{sol_str}", None)(
        str(input_path)
    )

    solution: Solution = getattr(class_module, f"Solution{sol_str}", None)(loader)

    print(solution.solution_1())
    print(solution.solution_2())


if __name__ == "__main__":
    main()
