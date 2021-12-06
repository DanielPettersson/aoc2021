from collections import Counter
from typing import TextIO, Any

from src.common.base_day import BaseDay


class Day06(BaseDay):

    def execute(self, input_file: TextIO) -> Any:
        fishes = dict(Counter(int(v) for v in input_file.readline().split(",")))
        for i in range(9):
            if i not in fishes:
                fishes[i] = 0

        for generation in range(256):
            births = fishes[0]
            for i in range(1, 9):
                fishes[i - 1] = fishes[i]
            fishes[6] += births
            fishes[8] = births

        return sum(fishes.values())


if __name__ == '__main__':
    Day06().run()
