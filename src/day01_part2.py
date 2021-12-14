from collections import deque
from typing import TextIO, Any

from src.common.base_day import BaseDay


class Day01(BaseDay):

    def execute(self, input_file: TextIO) -> Any:
        num_increased = 0
        values = deque([], 3)
        previous_values = deque([], 3)

        for line in input_file:
            values.append(int(line))
            if len(previous_values) == 3 and sum(values) > sum(previous_values):
                num_increased += 1
            previous_values.append(int(line))

        return num_increased


if __name__ == '__main__':
    Day01().run()
