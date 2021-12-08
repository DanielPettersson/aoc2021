from typing import TextIO, Any

from src.common.base_day import BaseDay


def _cost(length: int) -> int:
    return int(length * (length + 1) / 2)


class Day07(BaseDay):

    def execute(self, input_file: TextIO) -> Any:
        positions = [int(v) for v in input_file.readline().split(",")]
        avg_position = int(sum(positions) / len(positions))
        return sum([_cost(abs(pos - avg_position)) for pos in positions])


if __name__ == '__main__':
    Day07().run()
