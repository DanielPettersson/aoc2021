from dataclasses import dataclass
from typing import TextIO, Any, List, Tuple

from src.common.base_day import BaseDay


class BingoBoard:
    rows: List[List[str]]

    def __init__(self, rows: List[List[str]]):
        pass

    def mark_number(self, drawn_number: str):
        pass


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


        return ""


if __name__ == '__main__':
    Day04().run()
