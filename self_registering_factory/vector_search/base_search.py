from abc import abstractmethod
from enum import auto

from strenum import LowercaseStrEnum

from ..base import ModuleEngine


class VectorSearchName(LowercaseStrEnum):
    MongoDB = auto()
    ChromaDB = auto()


class VectorSearchEngine(ModuleEngine):
    """Base class for vector search engines."""

    @abstractmethod
    def add_vector(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_vector(self, *args, **kwargs):
        pass

    @abstractmethod
    def create_controller(self, *args, **kwargs):
        pass

    @abstractmethod
    def search_vector(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        return self.search_vector(*args, **kwargs)
