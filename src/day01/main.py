from collections import deque
from typing import Optional

from src import day01
from src.common.util import get_input


def part1():
    with get_input(day01) as input_file:

        num_increased = 0
        previous_value: Optional[int] = None

        for line in input_file:
            value = int(line)
            if previous_value and value > previous_value:
                num_increased += 1
            previous_value = value

        print(f"Number of increased values are {num_increased}")


def part2():
    with get_input(day01) as input_file:

        num_increased = 0
        values = deque([], 3)
        previous_values = deque([], 3)

        for line in input_file:
            values.append(int(line))
            if len(previous_values) == 3 and sum(values) > sum(previous_values):
                num_increased += 1
            previous_values.append(int(line))

        print(f"Number of increased values are {num_increased}")


if __name__ == '__main__':
    part1()
    part2()
