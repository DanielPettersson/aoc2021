from dataclasses import dataclass
from typing import TextIO, Any, List

from src.common.base_day import BaseDay


@dataclass
class BingoCell:
    number: str
    marked: bool

    def mark_if_match(self, drawn_number):
        if self.number == drawn_number:
            self.marked = True


class BingoBoard:
    rows: List[List[BingoCell]]

    def __init__(self, rows: List[List[str]]):
        self.rows = [[BingoCell(c, False) for c in r] for r in rows]

    def mark_number(self, drawn_number: str) -> None:
        for row in self.rows:
            for c in row:
                c.mark_if_match(drawn_number)

    def is_winner(self) -> bool:
        if self._is_winner(self.rows):
            return True
        cols = list(zip(*self.rows))
        return self._is_winner(cols)

    def sum_of_unmarked(self) -> int:
        return sum(int(c.number) for r in self.rows for c in r if not c.marked)

    @staticmethod
    def _is_winner(rows):
        for row in rows:
            if all(c.marked for c in row):
                return True


def parse_input(input_file: TextIO) -> (List[str], List[BingoBoard]):
    drawn_numbers = input_file.readline().split(",")
    bingo_boards = list()
    input_file.readline()

    board_lines = []
    for line in input_file:
        if not line.strip():
            bingo_boards.append(BingoBoard(board_lines))
            board_lines = []
        else:
            board_lines.append([num.strip() for num in line.split(" ") if num])
    if board_lines:
        bingo_boards.append(BingoBoard(board_lines))

    return drawn_numbers, bingo_boards


class Day04(BaseDay):

    def execute(self, input_file: TextIO) -> Any:
        drawn_numbers, bingo_boards = parse_input(input_file)

        for drawn_number in drawn_numbers:
            for bingo_board in bingo_boards:
                bingo_board.mark_number(drawn_number)

            winning_boards = [bb for bb in bingo_boards if bb.is_winner()]
            for winning_board in winning_boards:
                if len(bingo_boards) == 1:
                    return winning_board.sum_of_unmarked() * int(drawn_number)
                else:
                    bingo_boards.remove(winning_board)

        return ""


if __name__ == '__main__':
    Day04().run()
