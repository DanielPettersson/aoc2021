from typing import TextIO, Any, List, Tuple, Optional

from colorama import Fore
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

from src.common.base_day import BaseDay

VISITS = [(0, 1), (1, 0)]


class Day15(BaseDay):


    def execute(self, input_file: TextIO) -> Any:
        input_grid = [[int(c) for c in line.strip()] for line in input_file]
        size = len(input_grid)

        grid = Grid(matrix=input_grid)

        start = grid.node(0, 0)
        end = grid.node(size - 1, size - 1)

        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)

        self.print(input_grid, path)

        return sum(input_grid[y][x] for x, y in path[1:])

    @staticmethod
    def print(grid: List[List[int]], path: List[Tuple[int, int]]):
        size = len(grid)
        for y in range(0, size):
            for x in range(0, size):
                if (x, y) in path:
                    print(f"{Fore.RED}{grid[y][x]}{Fore.RESET}", end="")
                else:
                    print(grid[y][x], end="")
            print("")
        print("")


if __name__ == '__main__':
    Day15().run()
