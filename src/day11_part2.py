from typing import TextIO, Any, List, Tuple

from colorama import Fore

from src.common.base_day import BaseDay


class Day11(BaseDay):

    grid: List[List[int]]
    width: int
    height: int

    def execute(self, input_file: TextIO) -> Any:
        self.grid = [[int(v) for v in line.strip()] for line in input_file]
        self.height = len(self.grid)
        self.width = len(self.grid[0])

        step = 0
        while True:
            step += 1

            for y in range(self.height):
                for x in range(self.width):
                    self.grid[y][x] += 1

            flashes = []
            while True:
                any_flashes = False
                for y in range(self.height):
                    for x in range(self.width):
                        if self.grid[y][x] > 9 and (x, y) not in flashes:
                            any_flashes = True
                            flashes.append((x, y))
                            for xx, yy in self.get_neighbor_coords(x, y):
                                self.grid[yy][xx] += 1
                if not any_flashes:
                    break

            for x, y in flashes:
                self.grid[y][x] = 0

            self.print()

            if len(flashes) == self.width * self.height:
                break

        return step

    def get_neighbor_coords(self, x: int, y: int) -> List[Tuple[int, int]]:
        ret = []
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                xx = x + dx
                yy = y + dy
                if xx == x and yy == y:
                    continue
                if xx < 0 or xx >= self.width:
                    continue
                if yy < 0 or yy >= self.height:
                    continue
                ret.append((xx, yy))
        return ret

    def print(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.grid[y][x] == 0:
                    print(f"{Fore.YELLOW}{self.grid[y][x]}{Fore.RESET}", end="")
                else:
                    print(self.grid[y][x], end="")
            print("")
        print("")


if __name__ == '__main__':
    Day11().run()
