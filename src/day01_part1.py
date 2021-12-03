from collections import deque
from typing import TextIO, Any, Optional

from src.common.base_day import BaseDay


class Day01(BaseDay):

    def execute(self, input_file: TextIO) -> Any:
        num_increased = 0
        previous_value = None

        for line in input_file:
            value = int(line)
            if previous_value and value > previous_value:
                num_increased += 1
            previous_value = value

        return num_increased


if __name__ == '__main__':
    Day01().run()
