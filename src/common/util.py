import importlib.resources
from types import ModuleType
from typing import TextIO


def get_input(module: ModuleType) -> TextIO:
    module_path = f"{module.__name__}.resources"
    return importlib.resources.open_text(module_path, "input.txt", encoding="utf-8")
