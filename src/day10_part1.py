from dataclasses import dataclass
from typing import TextIO, Any

from src.common.base_day import BaseDay

CHUNKS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

ILLEGAL_SCORE = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


class IncompleteChunkError(Exception):
    pass


@dataclass
class IllegalChunkError(Exception):
    character: str
    pos: int


class Day10(BaseDay):

    def execute(self, input_file: TextIO) -> Any:
        return sum(self.parse_line(line.strip()) for line in input_file)

    def parse_line(self, line: str) -> int:
        try:
            self.parse_chunk(line, 0)
        except IllegalChunkError as e:
            print(f"Illegal line at pos {e.pos}, not expected {e.character}: {line}")
            return ILLEGAL_SCORE.get(e.character)
        except IncompleteChunkError:
            print(f"Incomplete line: {line}")
            return 0
        print(f"Good line: {line}")
        return 0

    def parse_chunk(self, line: str, pos: int) -> int:
        char = self.get_char(line, pos)
        next_pos = pos + 1
        if char in CHUNKS:
            next_char = self.get_char(line, next_pos)

            if next_char == CHUNKS[char]:
                return next_pos
            elif next_char in CHUNKS:
                end_pos = next_pos
                while next_char in CHUNKS:
                    end_pos = self.parse_chunk(line, next_pos)
                    next_pos = end_pos + 1
                    next_char = self.get_char(line, next_pos)
                if next_char == CHUNKS[char]:
                    return end_pos + 1
                else:
                    raise IllegalChunkError(next_char, end_pos + 1)

            else:
                raise IllegalChunkError(next_char, next_pos)

        else:
            raise IllegalChunkError(char, pos)

    @staticmethod
    def get_char(line: str, pos: int) -> str:
        try:
            return line[pos]
        except IndexError:
            raise IncompleteChunkError()


if __name__ == '__main__':
    Day10().run()
