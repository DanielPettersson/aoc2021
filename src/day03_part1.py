from collections import Counter
from typing import TextIO, Any

from src.common.base_day import BaseDay


class Day03(BaseDay):

    def execute(self, input_file: TextIO) -> Any:
        rows = [list(line) for line in input_file]
        cols = list(zip(*rows))

        gammas = []
        epsilons = []
        for col in cols:
            most_common = Counter(col).most_common(2)
            gammas.append(most_common[0][0])
            epsilons.append(most_common[1][0])

        gamma = int("".join(gammas), base=2)
        epsilon = int("".join(epsilons), base=2)

        return gamma * epsilon


if __name__ == '__main__':
    Day03().run()
