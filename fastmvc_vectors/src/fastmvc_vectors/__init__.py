"""
fastmvc_vectors – Vector stores (Pinecone, Qdrant, Weaviate) for FastMVC.
"""

from fastmvc_core import (
    VectorsConfiguration,
    VectorsConfigurationDTO,
    PineconeConfigDTO,
    QdrantConfigDTO,
    WeaviateConfigDTO,
)

from .base import IVectorStore, build_vector_store

__version__ = "0.1.0"

__all__ = [
    "IVectorStore",
    "VectorsConfiguration",
    "VectorsConfigurationDTO",
    "PineconeConfigDTO",
    "QdrantConfigDTO",
    "WeaviateConfigDTO",
    "build_vector_store",
]
