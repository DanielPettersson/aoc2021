from dataclasses import dataclass
from typing import TextIO, Any

from src.common.base_day import BaseDay


@dataclass
class Position:
    aim: int
    pos: int
    depth: int


class Day02(BaseDay):

    def execute(self, input_file: TextIO) -> Any:
        pos = Position(0, 0, 0)

        for line in input_file:
            cmd, param = line.split(" ")
            self.cmds[cmd](int(param), pos)

        return pos.pos * pos.depth

    @staticmethod
    def move_forward(steps: int, position: Position):
        position.pos += steps
        position.depth += steps * position.aim

    @staticmethod
    def move_down(steps: int, position: Position):
        position.aim += steps

    @staticmethod
    def move_up(steps: int, position: Position):
        position.aim -= steps

    cmds = {
        'forward': move_forward,
        'up': move_up,
        'down': move_down
    }


if __name__ == '__main__':
    Day02().run()
