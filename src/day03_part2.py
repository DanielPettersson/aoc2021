from collections import Counter
from typing import TextIO, Any, Iterable, List, Optional

from src.common.base_day import BaseDay


class Day03(BaseDay):

    def execute(self, input_file: TextIO) -> Any:
        rows = [list(line) for line in input_file]
        oxygen_ratings = self.get_val(rows, tie_value='1', n=0)
        co2_scrubber_ratings = self.get_val(rows, tie_value='0', n=1)

        oxygen_rating = int("".join(oxygen_ratings), base=2)
        co2_scrubber_rating = int("".join(co2_scrubber_ratings), base=2)
        return oxygen_rating * co2_scrubber_rating

    def get_val(self, rows: List[List[str]], tie_value: str, n: int, col: Optional[int] = None):

        if not col:
            col = 0

        if len(rows) == 1:
            return rows[0]

        cols = list(zip(*rows))
        common = self.nth_common(cols[col], n, tie_value)

        new_rows = [r for r in rows if r[col] == common]
        return self.get_val(new_rows, tie_value, n, col=col + 1)

    @staticmethod
    def nth_common(items: Iterable[str], n: int, tie_value: str):
        assert 0 <= n <= 1
        most_common = Counter(items).most_common(2)
        if most_common[0][1] == most_common[1][1]:
            return tie_value
        else:
            return most_common[n][0]


if __name__ == '__main__':
    Day03().run()
