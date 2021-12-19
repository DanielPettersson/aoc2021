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

        dx1 = 1
        x = target.x1
        while x >= 0:
            x -= dx1
            dx1 += 1
        dx2 = target.x2 + 1

        possible_initial_velocities: List[Tuple[int, int]] = []

        for dy in range(target.y1, 200):
            for dx in range(dx1, dx2 + 1):
                probe = Probe(0, 0, dx, dy)
                while not probe.is_beyond(target) and not probe.is_in(target):
                    probe.update_speed()
                    probe.update_position()
                if probe.is_in(target):
                    possible_initial_velocities.append((dx, dy))

        return len(possible_initial_velocities)


if __name__ == '__main__':
    Day17().run()
