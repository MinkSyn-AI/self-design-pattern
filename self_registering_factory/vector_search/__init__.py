from typing import Dict, Type

from ..base import BaseFactoryModule, ModuleEngine
from .base_search import VectorSearchName
from .chroma_db import ChromaDBVectorEngine
from .mongo_db import MongoDBVectorEngine


class AutoVectorSearchModule(BaseFactoryModule):
    @property
    def _module_mapping(self) -> Dict[VectorSearchName, Type[ModuleEngine]]:
        return {
            VectorSearchName.ChromaDB: ChromaDBVectorEngine,
            VectorSearchName.MongoDB: MongoDBVectorEngine,
        }
