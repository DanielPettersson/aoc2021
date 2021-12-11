import importlib.resources
from abc import ABC, abstractmethod
from datetime import time
from time import perf_counter
from typing import TextIO, Any


class BaseDay(ABC):
    def get_input(self) -> TextIO:
        return importlib.resources.open_text('resources', f"{self.__class__.__name__}.txt", encoding="utf-8")

    @abstractmethod
    def execute(self, input_file: TextIO) -> Any:
        pass

    def run(self):
        with self.get_input() as input_file:
            tic = perf_counter()
            print(f"Answer is: {self.execute(input_file)}")
            toc = perf_counter()
            print(f"Executed in {toc - tic:0.4f} seconds")

