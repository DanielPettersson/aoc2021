import importlib.resources
from abc import ABC, abstractmethod
from typing import TextIO, Any


class BaseDay(ABC):
    def get_input(self) -> TextIO:
        return importlib.resources.open_text('resources', f"{self.__class__.__name__}.txt", encoding="utf-8")

    @abstractmethod
    def execute(self, input_file: TextIO) -> Any:
        pass

    def run(self):
        with self.get_input() as input_file:
            print(self.execute(input_file))
