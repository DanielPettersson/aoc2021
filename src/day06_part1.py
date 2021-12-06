from typing import TextIO, Any

from src.common.base_day import BaseDay


class Day06(BaseDay):

    def execute(self, input_file: TextIO) -> Any:
        fishes = [int(v) for v in input_file.readline().split(",")]

        for generation in range(80):
            new_fishes = []
            for i, fish in enumerate(fishes):
                if fish == 0:
                    fishes[i] = 6
                    new_fishes.append(8)
                else:
                    fishes[i] = fish - 1
            fishes = fishes + new_fishes

        return len(fishes)


if __name__ == '__main__':
    Day06().run()
