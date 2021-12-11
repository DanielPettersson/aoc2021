from dataclasses import dataclass
from statistics import median
from typing import TextIO, Any, Optional, List

from src.common.base_day import BaseDay

CHUNKS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

COMPLETION_SCORE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


@dataclass
class IllegalChunkError(Exception):
    character: str
    pos: int


class Day10(BaseDay):

    def execute(self, input_file: TextIO) -> Any:
        completion_scores = [self.parse_line(line.strip()) for line in input_file]
        completion_scores = [s for s in completion_scores if s]
        return median(completion_scores)

    def parse_line(self, line: str) -> Optional[int]:
        try:
            completion = []
            self.parse_chunk(line, completion, 0)
            if completion:
                completion_str = ''.join(completion)
                print(f"Incomplete line: {line}, needs {completion_str} to complete")

                completion_score = 0
                for char in completion_str:
                    completion_score *= 5
                    completion_score += COMPLETION_SCORE[char]
                return completion_score

            else:
                print(f"Good line: {line}")
                return None
        except IllegalChunkError as e:
            print(f"Illegal line at pos {e.pos}, not expected {e.character}: {line}")
            return None

    def parse_chunk(self, line: str, completion: List[str], pos: int) -> int:
        char = self.get_char(line, pos, None, completion)
        next_pos = pos + 1
        if char in CHUNKS:
            next_char = self.get_char(line, next_pos, CHUNKS[char], completion)

            if next_char == CHUNKS[char]:
                return next_pos
            elif next_char in CHUNKS:
                end_pos = next_pos
                while next_char in CHUNKS:
                    end_pos = self.parse_chunk(line, completion, next_pos)
                    next_pos = end_pos + 1
                    next_char = self.get_char(line, next_pos, CHUNKS[char], completion)
                if next_char == CHUNKS[char]:
                    return end_pos + 1
                else:
                    raise IllegalChunkError(next_char, end_pos + 1)

            else:
                raise IllegalChunkError(next_char, next_pos)

        else:
            raise IllegalChunkError(char, pos)

    @staticmethod
    def get_char(line: str, pos: int, expected_char: Optional[str], completion: List[str]) -> str:
        try:
            return line[pos]
        except IndexError as e:
            if expected_char:
                completion.append(expected_char)
                return expected_char
            else:
                raise e


if __name__ == '__main__':
    Day10().run()
