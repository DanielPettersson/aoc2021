import os
from abc import ABC, abstractmethod
from time import perf_counter
from typing import TextIO, Any

import requests


class BaseDay(ABC):

    def get_input(self) -> TextIO:
        try:
            return self._read_input_from_file()
        except FileNotFoundError:
            input_str = self._get_input_from_request()
            self._write_input_to_file(input_str)
            return self._read_input_from_file()

    def _write_input_to_file(self, input_str: str):
        with open(self._get_input_file_name(), "w") as input_file:
            input_file.write(input_str)

    def _get_input_from_request(self):
        token = self._get_token()
        return requests.get(
            f"https://adventofcode.com/2021/day/{self._get_day_number()}/input",
            cookies={"session": token}
        ).text

    def _read_input_from_file(self) -> TextIO:
        return open(self._get_input_file_name(), mode="r")

    def _get_input_file_name(self) -> str:
        return self._get_input_file_path(f"{self.__class__.__name__}.txt")

    def _get_day_number(self) -> int:
        return int(self.__class__.__name__[3:])

    def _get_token(self) -> str:
        token_path = self._get_input_file_path(f"token.txt")
        try:
            with open(token_path, "r") as token_file:
                return token_file.readline().strip()
        except FileNotFoundError:
            raise FileNotFoundError(f"Expected {token_path} with Advent of Code session token in it")

    @staticmethod
    def _get_input_file_path(name: str) -> str:
        return os.path.expanduser(f"~/.aoc/{name}")

    @abstractmethod
    def execute(self, input_file: TextIO) -> Any:
        pass

    def run(self):
        with self.get_input() as input_file:
            tic = perf_counter()
            print(f"Answer is: {self.execute(input_file)}")
            toc = perf_counter()
            print(f"Executed in {toc - tic:0.4f} seconds")
