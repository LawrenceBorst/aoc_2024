from pathlib import Path, PosixPath
from .solution_01 import Solution01, DataLoader01

def main():
    base_path: PosixPath = Path(__file__).parent
    input_path = (base_path / "solution_01" / "input.txt").resolve()
    loader: DataLoader01 = DataLoader01(str(input_path))
    solution: Solution01 = Solution01(loader)

    if (solution):
        print('Success!')



if __name__ == '__main__':
    main()