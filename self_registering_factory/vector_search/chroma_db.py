from typing import Any, Optional

from .base_search import VectorSearchEngine


class ChromaDBVectorEngine(VectorSearchEngine):
    @classmethod
    def build(
        cls,
        name: str = "Alibaba-NLP/gte-multilingual-base",
        path: str = "./chroma_db",
        limit: int = 12,
        **kwargs,
    ) -> VectorSearchEngine:
        try:
            instance = cls()
            # Init ChromaDB client here
            instance.client = ...  # chromadb.Client()

            # Get or create a collection in ChromaDB
            instance.collection = (
                ...
            )  # instance.client.get_or_create_collection(name=path)

            instance.limit = limit

        except Exception as e:
            raise ValueError(f"ChromaDB failed to initialize. Error: {e}") from e

        return instance

    def search_vector(
        self, query_vector: Any, limit_embedding: Optional[int] = None, **kwargs
    ):
        # Implement the logic to search for similar vectors in ChromaDB
        pass

    def add_vector(self, embedding_vector: Any, **kwargs):
        pass

    def delete_vector(self, vector_id: str, **kwargs):
        pass

    def create_controller(self, name_controller: str, **kwargs):
        pass

    def is_healthy(self) -> bool:
        # Implement health check logic for ChromaDB connection
        return True
