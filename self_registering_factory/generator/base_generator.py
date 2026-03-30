from abc import abstractmethod
from enum import auto

from strenum import LowercaseStrEnum

from ..base import ModuleEngine


class GeneratorType(LowercaseStrEnum):
    ONLINE = auto()  # Calling with API protocol
    OFFLINE = auto()  # Building at local server


class GeneratorName(LowercaseStrEnum):
    Gemini = auto()
    Qwen = auto()


class GeneratorEngine(ModuleEngine):
    """Base class for generator search engines."""

    @abstractmethod
    def generate(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        return self.generate(*args, **kwargs)
