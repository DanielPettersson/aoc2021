from collections import deque
from dataclasses import dataclass
from typing import TextIO, Any, Optional, Dict

from src.common.base_day import BaseDay


def _range(start, end, step):
    end += step
    return range(start, end, step)


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

    def trace(self):

        s = self.start
        e = self.end

        x_step = 1 if e.x > s.x else -1 if s.x > e.x else 0
        y_step = 1 if e.y > s.y else -1 if s.y > e.y else 0

        assert x_step != 0 or y_step != 0

        if x_step == 0:
            y_range = _range(s.y, e.y, y_step)
            x_range = [s.x for i in y_range]
        elif y_step == 0:
            x_range = _range(s.x, e.x, x_step)
            y_range = [s.y for i in x_range]
        else:
            x_range = _range(s.x, e.x, x_step)
            y_range = _range(s.y, e.y, y_step)

        for x, y in zip(x_range, y_range):
            yield Point(x, y)

    @staticmethod
    def _parse_input_str(input_str: str) -> (int, int):
        return [int(v) for v in input_str.split(",")]


class Day05(BaseDay):

    def execute(self, input_file: TextIO) -> Any:
        vectors = [Vector(*line.split(" -> ")) for line in input_file]

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
