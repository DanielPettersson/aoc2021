from collections import deque
from dataclasses import dataclass
from typing import TextIO, Any, Optional, Dict

from src.common.base_day import BaseDay


@dataclass(eq=True, frozen=True)
class Point:
    x: int
    y: int


class Vector:
    start: Point
    end: Point

    def __init__(self, start_str: str, end_str: str):
        self.start = Point(*self._parse_input_str(start_str))
        self.end = Point(*self._parse_input_str(end_str))

    def __repr__(self):
        return f"start: {self.start}, end: {self.end}"

    def is_horizontal_or_vertical(self) -> bool:
        return self._is_horizontal() or self._is_vertical()

    def trace(self):
        if self._is_horizontal():
            xs = min(self.start.x, self.end.x)
            xe = max(self.start.x, self.end.x)

            for x in range(xs, xe + 1):
                yield Point(x, self.start.y)

        elif self._is_vertical():
            ys = min(self.start.y, self.end.y)
            ye = max(self.start.y, self.end.y)

            for y in range(ys, ye + 1):
                yield Point(self.start.x, y)

        else:
            raise ValueError("No support for non vertical or horizontal vectors")

    def _is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    def _is_vertical(self) -> bool:
        return self.start.x == self.end.x


    @staticmethod
    def _parse_input_str(input_str: str) -> (int, int):
        return [int(v) for v in input_str.split(",")]


class Day05(BaseDay):

    def execute(self, input_file: TextIO) -> Any:
        vectors = [Vector(*line.split(" -> ")) for line in input_file]
        vectors = [v for v in vectors if v.is_horizontal_or_vertical()]

        points_map: Dict[Point, int] = dict()
        for v in vectors:
            for p in v.trace():
                if p not in points_map:
                    points_map[p] = 0
                points_map[p] += 1

        points_map = {k: v for k, v in points_map.items() if v > 1}
        return len(points_map)


if __name__ == '__main__':
    Day05().run()
