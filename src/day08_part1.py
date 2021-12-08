from typing import TextIO, Any

from src.common.base_day import BaseDay

NUM_SEGMENTS_TO_DIGITS = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8]
}


class Day08(BaseDay):

    def execute(self, input_file: TextIO) -> Any:

        count = 0
        for line in input_file:
            for digit in line.split(" | ")[1].split(" "):
                count += 1 if len(NUM_SEGMENTS_TO_DIGITS[len(digit.strip())]) == 1 else 0

        return count


if __name__ == '__main__':
    Day08().run()
