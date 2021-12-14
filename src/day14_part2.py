from typing import TextIO, Any, Dict

from src.common.base_day import BaseDay


class Day14(BaseDay):

    def execute(self, input_file: TextIO) -> Any:
        template = input_file.readline().strip()
        input_file.readline()
        rules = {}
        for line in input_file:
            k, v = line.strip().split(" -> ")
            rules[k] = v

        t_map = {}
        for i in range(len(template) - 1):
            pair = template[i: i + 2]
            self.add_to_map(t_map, pair, 1)

        for step in range(40):
            res = {}
            for pair, num in t_map.items():
                r = rules[pair]
                self.add_to_map(res, pair[0] + r, num)
                self.add_to_map(res, r + pair[1], num)
            t_map = res

        char_map = {}
        for pair, num in t_map.items():
            self.add_to_map(char_map, pair[0], num)

        num_most_common = max(char_map.values())
        num_least_common = min(char_map.values())

        return num_most_common - num_least_common + 1

    @staticmethod
    def add_to_map(m: Dict[str, int], p: str, num: int):
        if p not in m:
            m[p] = 0
        m[p] += num


if __name__ == '__main__':
    Day14().run()
