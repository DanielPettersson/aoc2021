import re
from dataclasses import dataclass, field
from typing import TextIO, Any, Tuple, List

from src.common.base_day import BaseDay


@dataclass
class Target:
    x1: int
    x2: int
    y1: int
    y2: int

    def is_in(self, x: int, y: int) -> bool:
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2


@dataclass
class Probe:
    x: int
    y: int
    dx: int
    dy: int
    positions: List[Tuple[int, int]] = field(default_factory=list)

    def update_speed(self):
        if self.dx > 0:
            self.dx -= 1
        if self.dx < 0:
            self.dx += 1
        self.dy -= 1

    def update_position(self):
        if not self.positions:
            self.positions.append((self.x, self.y))

        self.x += self.dx
        self.y += self.dy

        self.positions.append((self.x, self.y))

    def is_in(self, target: Target) -> bool:
        return target.is_in(self.x, self.y)

    def is_beyond(self, target: Target) -> bool:
        return target.x2 < self.x or self.y < target.y1


class Day17(BaseDay):

    def execute(self, input_file: TextIO) -> Any:
        target_str = input_file.readline().strip()
        rgx = re.search('target area: x=(-*\\d+)\\.\\.(-*\\d+), y=(-*\\d+)\\.\\.(-*\\d+)', target_str)
        target = Target(int(rgx.group(1)), int(rgx.group(2)), int(rgx.group(3)), int(rgx.group(4)))

        dx = 1
        x = target.x1
        while x >= 0:
            x -= dx
            dx += 1

        mdy = 0
        for dy in range(500):
            probe = Probe(0, 0, dx, dy)
            while not probe.is_beyond(target) and not probe.is_in(target):
                probe.update_speed()
                probe.update_position()
            if probe.is_in(target):
                mdy = dy

        probe = Probe(0, 0, dx, mdy)
        while not probe.is_beyond(target) and not probe.is_in(target):
            probe.update_speed()
            probe.update_position()

        # self.print(target, probe)
        print(f"probe hit: {probe.is_in(target)}, target: {target}, probe: {probe}")
        print(f"mdy: {mdy}")
        max_y = max(y for x, y in probe.positions)
        return max_y

    @staticmethod
    def print(target: Target, probe: Probe):
        min_y = min(y for x, y in probe.positions)
        max_y = max(y for x, y in probe.positions)
        min_x = min(x for x, y in probe.positions)
        max_x = max(x for x, y in probe.positions)

        for y in range(max_y, min_y - 1, -1):
            for x in range(min_x, max_x + 1):
                if x == 0 and y == 0:
                    print("S", end="")
                elif (x, y) in probe.positions:
                    print("#", end="")
                elif target.is_in(x, y):
                    print("T", end="")
                else:
                    print(".", end="")
            print()


if __name__ == '__main__':
    Day17().run()
