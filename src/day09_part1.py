from typing import TextIO, Any

from src.common.base_day import BaseDay


class Day09(BaseDay):

    def execute(self, input_file: TextIO) -> Any:
        height_map = [[int(v) for v in line.strip()] for line in input_file]

        width = len(height_map[0])
        height = len(height_map)

        risk_sum = 0

        for y in range(0, height):
            for x in range(0, width):
                larger_neighbors = 0
                for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                    xx = x + dx
                    yy = y + dy
                    if 0 <= xx < width and 0 <= yy < height:
                        larger_neighbors += 1 if height_map[y][x] < height_map[yy][xx] else 0
                    else:
                        larger_neighbors += 1
                if larger_neighbors == 4:
                    risk_sum += height_map[y][x] + 1

        return risk_sum


if __name__ == '__main__':
    Day09().run()
