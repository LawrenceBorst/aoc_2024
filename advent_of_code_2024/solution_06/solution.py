from typing import Tuple
from ..utils.solution import Solution
from .data_loader import Data, Coord
from enum import IntEnum


class Direction(IntEnum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3


class Solution06(Solution[int, Data]):
    _map: list[Coord]
    _height: int
    _width: int
    _visits: set[Coord]
    _start: Coord

    def __init__(self, data_loader):
        super().__init__(data_loader)

        self._map, self._start = self._data
        self._height = max([y for (_, y) in self._map])
        self._width = max([x for (x, _) in self._map])
        self._visits = set()

    def solution_1(self) -> int:
        current_pos: Coord = self._start
        dir = Direction.Up
        hit_wall: bool = True

        while hit_wall:
            next_pos, dir, hit_wall = self._get_next_state(current_pos, dir)
            self._update_visits(current_pos, next_pos)

            current_pos = next_pos

        # +1 because start is not counted
        return len(self._visits) + 1

    def solution_2(self) -> int:
        return NotImplemented

    def _get_next_state(
        self, pos: Coord, dir: Direction
    ) -> Tuple[Coord, Direction, bool]:
        """
        Returns the next position, direction and whether a wall is hit
        """
        next_pos: Coord
        hit_wall: bool = True

        next_blocks: list[Coord] = self._get_next_blocks(pos, dir)

        if len(next_blocks) == 0:
            return self._get_next_pos_no_wall(pos, dir), dir, False

        next_block: Coord = self._get_next_block(next_blocks, dir)

        next_pos: Coord = self._get_next_pos(next_block, dir)

        dir = self._update_dir(dir)

        return next_pos, dir, hit_wall

    def _get_next_blocks(self, pos: Coord, dir: Direction) -> list[Coord]:
        if dir == Direction.Up:
            return [x for x in self._map if x[0] < pos[0] and x[1] == pos[1]]
        elif dir == Direction.Right:
            return [x for x in self._map if x[0] == pos[0] and x[1] > pos[1]]
        elif dir == Direction.Down:
            return [x for x in self._map if x[0] > pos[0] and x[1] == pos[1]]
        elif dir == Direction.Left:
            return [x for x in self._map if x[0] == pos[0] and x[1] < pos[1]]

        raise ValueError("Invalid direction")

    def _get_next_block(self, next_blocks: list[Coord], dir: Direction) -> Coord:
        if dir == Direction.Up:
            return max(next_blocks, key=lambda y: y[0])
        elif dir == Direction.Right:
            return min(next_blocks, key=lambda x: x[1])
        elif dir == Direction.Down:
            return min(next_blocks, key=lambda y: y[0])
        elif dir == Direction.Left:
            return max(next_blocks, key=lambda x: x[1])

        raise ValueError("Invalid direction")

    def _get_next_pos_no_wall(self, pos: Coord, dir: Direction) -> Coord:
        """Get the next position given that there is no wall in the given direction"""
        if dir == Direction.Up:
            return (0, pos[1])
        elif dir == Direction.Right:
            return (pos[0], self._width)
        elif dir == Direction.Down:
            return (self._height, pos[1])
        elif dir == Direction.Left:
            return (pos[0], 0)

        raise ValueError("Invalid direction")

    def _get_next_pos(self, next_block: Coord, dir: Direction) -> Coord:
        if dir == Direction.Up:
            return (next_block[0] + 1, next_block[1])
        elif dir == Direction.Right:
            return (next_block[0], next_block[1] - 1)
        elif dir == Direction.Down:
            return (next_block[0] - 1, next_block[1])
        elif dir == Direction.Left:
            return (next_block[0], next_block[1] + 1)

        raise ValueError("Invalid direction")

    def _update_dir(self, dir: Direction) -> Direction:
        dir += 1
        return Direction(dir % 4)

    def _update_visits(self, start: Coord, end: Coord) -> None:
        if start[0] == end[0]:
            self._visits = self._visits.union(
                set(
                    [
                        (start[0], x)
                        for x in range(start[1], end[1], 1 if start[1] < end[1] else -1)
                    ]
                )
            )

            return

        elif start[1] == end[1]:
            self._visits = self._visits.union(
                set(
                    [
                        (y, start[1])
                        for y in range(start[0], end[0], 1 if start[0] < end[0] else -1)
                    ]
                )
            )

            return

        raise ValueError("Start and end not in the same row/column")
