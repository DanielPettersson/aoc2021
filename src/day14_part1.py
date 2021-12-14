from collections import Counter
from typing import TextIO, Any

from src.common.base_day import BaseDay


class Day14(BaseDay):

    def execute(self, input_file: TextIO) -> Any:
        template = input_file.readline().strip()
        input_file.readline()
        rules = {}
        for line in input_file:
            k, v = line.strip().split(" -> ")
            rules[k] = v

        for step in range(10):
            print(template)
            res = ""
            for i in range(len(template) - 1):
                pair = template[i: i + 2]
                r = rules[pair]
                rr = pair[0] + r
                res += rr
            template = res + template[-1]

        common_elements = Counter(template).most_common()
        num_most_common = common_elements[0][1]
        num_least_common = common_elements[-1][1]

        return num_most_common - num_least_common


if __name__ == '__main__':
    Day14().run()
