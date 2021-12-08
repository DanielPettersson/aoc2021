from statistics import median
from typing import TextIO, Any

from src.common.base_day import BaseDay


class Day07(BaseDay):

    def execute(self, input_file: TextIO) -> Any:
        positions = [int(v) for v in input_file.readline().split(",")]
        median_position = int(median(positions))
        return sum([abs(pos - median_position) for pos in positions])


if __name__ == '__main__':
    Day07().run()
