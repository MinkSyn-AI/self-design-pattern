import os
from typing import Any, Optional

from .base_search import VectorSearchEngine


class MongoDBVectorEngine(VectorSearchEngine):
    @classmethod
    def build(
        cls,
        name: str = "mongo-dev",
        mongodbUri: Optional[str] = None,
        mongoCollection: Optional[str] = None,
        limit: int = 12,
        **kwargs,
    ) -> VectorSearchEngine:
        try:
            if mongodbUri is None:
                mongodbUri = "mongodb://{}:{}@{}:{}/?authSource={}".format(
                    os.getenv("MONGO_DB_USER", kwargs.get("db_user", "root")),
                    os.getenv("MONGO_DB_PASS", kwargs.get("db_pass", "example")),
                    os.getenv("MONGO_DB_HOST", kwargs.get("db_host", "localhost")),
                    os.getenv("MONGO_DB_PORT", kwargs.get("db_port", "27017")),
                    os.getenv("MONGO_DB_AUTH", kwargs.get("db_auth", "admin")),
                )
            instance = cls()
            # Init MongoDB client here
            instance.client = ...  # pymongo.MongoClient(mongodbUri)

            instance.db = instance.client[name]
            instance.collection_name = mongoCollection
            instance.collection = instance.db[mongoCollection]

            instance.limit = limit

        except Exception as e:
            raise ValueError(f"MongoDB failed to initialize. Error: {e}") from e

        return instance

    def search_vector(
        self, query_vector: Any, limit_embedding: Optional[int] = None, **kwargs
    ):
        # Implement the logic to search for similar vectors in MongoDB
        pass

    def add_vector(self, embedding_vector: Any, **kwargs):
        pass

    def delete_vector(self, vector_id: str, **kwargs):
        pass

    def create_controller(self, name_controller: str, **kwargs):
        pass

    def is_healthy(self) -> bool:
        # Implement health check logic for MongoDB connection
        return True
