from itertools import permutations
from typing import TextIO, Any, Dict

from src.common.base_day import BaseDay

DIGITS = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}

SEGMENTS = ["a", "b", "c", "d", "e", "f", "g"]


def _map(digit: str, mapping: Dict[str, str]) -> str:
    return "".join(sorted([mapping[c] for c in digit]))


class Day08(BaseDay):

    def execute(self, input_file: TextIO) -> Any:

        count = 0
        for line in input_file:

            pattern_str, output_str = line.split(" | ")
            patterns = [s.strip() for s in pattern_str.split(" ")]
            outputs = [s.strip() for s in output_str.split(" ")]

            mapping = {}
            for perm in permutations(SEGMENTS):
                mapping = {s[0]: s[1] for s in zip(SEGMENTS, perm)}

                num_matched = 0
                for pattern in patterns:
                    mapped_pattern = _map(pattern, mapping)
                    num_matched += 1 if mapped_pattern in DIGITS else 0

                if num_matched == len(patterns):
                    break
                else:
                    mapping = {}

            value = int("".join([DIGITS[_map(d, mapping)] for d in outputs]))
            print(f"{mapping}\t{value}")
            count += value

        return count


if __name__ == '__main__':
    Day08().run()
