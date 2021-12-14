from typing import TextIO, Any, List, Tuple, Callable

from colorama import Fore

from src.common.base_day import BaseDay


class Day09(BaseDay):
    height_map: List[List[int]]
    width: int
    height: int
    low_points: List[Tuple[int, int]]
    basins: List[List[Tuple[int, int]]]

    def execute(self, input_file: TextIO) -> Any:
        self.height_map = [[int(v) for v in line.strip()] for line in input_file]
        self.width = len(self.height_map[0])
        self.height = len(self.height_map)
        self.low_points = []
        self.basins = []

        for y in range(0, self.height):
            for x in range(0, self.width):
                larger_neighbors = sum(self._visit_neighbors(
                    x, y,
                    lambda xx, yy: 1 if self.height_map[y][x] < self.height_map[yy][xx] else 0,
                    lambda: 1
                ))
                if larger_neighbors == 4:
                    self.low_points.append((x, y))

        for low_point in self.low_points:
            basin_coords = []
            self._find_basin(basin_coords, low_point[0], low_point[1])
            self.basins.append(basin_coords)

        sorted_basins = sorted(self.basins, key=lambda b: len(b), reverse=True)
        self._print_output()

        return len(sorted_basins[0]) * len(sorted_basins[1]) * len(sorted_basins[2])

    def _print_output(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                coord = (x, y)
                if coord in self.low_points:
                    print(f"{Fore.RED}{self.height_map[y][x]}{Fore.RESET}", end="")
                elif self._is_coord_in_basin(coord):
                    print(f"{Fore.BLUE}{self.height_map[y][x]}{Fore.RESET}", end="")
                else:
                    print(self.height_map[y][x], end="")
            print("")

    def _is_coord_in_basin(self, coord: Tuple[int, int]) -> bool:
        for basin_coords in self.basins:
            if coord in basin_coords:
                return True
        return False

    def _find_basin(self, basin_coords: List[Tuple[int, int]], x: int, y: int) -> None:
        def visit_in_range(xx: int, yy: int) -> None:
            if self.height_map[yy][xx] < 9 and (xx, yy) not in basin_coords:
                basin_coords.append((xx, yy))
                self._find_basin(basin_coords, xx, yy)

        self._visit_neighbors(
            x, y,
            visit_in_range,
            lambda: None
        )

    def _visit_neighbors(self, x: int, y: int,
                         visit_in_range: Callable[[int, int], Any],
                         visit_out_of_range: Callable[[], Any]):
        res = []
        for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            xx = x + dx
            yy = y + dy
            if 0 <= xx < self.width and 0 <= yy < self.height:
                res.append(visit_in_range(xx, yy))
            else:
                res.append(visit_out_of_range())
        return res


if __name__ == '__main__':
    Day09().run()
