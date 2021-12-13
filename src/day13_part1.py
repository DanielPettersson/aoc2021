from pprint import pprint
from typing import TextIO, Any, Tuple, Set, List

from src.common.base_day import BaseDay


class Day13(BaseDay):

    def execute(self, input_file: TextIO) -> Any:

        dots: Set[Tuple[int, int]] = set()
        folds: List[Tuple[str, int]] = []

        while True:
            line = input_file.readline().strip()
            if not line:
                break
            x, y = line.split(",")
            dots.add((int(x), int(y)))

        while True:
            line = input_file.readline().strip()
            if not line:
                break

            along, val = line[11:].split("=")
            folds.append((along, int(val)))

        pprint(dots)
        pprint(folds)

        dots = self.fold(dots,  folds[0])

        return len(dots)

    @staticmethod
    def fold(dots: Set[Tuple[int, int]], f: Tuple[str, int]) -> Set[Tuple[int, int]]:
        along, val = f
        ret: Set[Tuple[int, int]] = set()

        for dot in dots:
            x, y = dot
            if along == "x":
                if x > val:
                    ret.add((x - (x - val) * 2, y))
                else:
                    ret.add((x, y))
            elif along == "y":
                if y > val:
                    ret.add((x, y - (y - val) * 2))
                else:
                    ret.add((x, y))

        return ret


if __name__ == '__main__':
    Day13().run()
