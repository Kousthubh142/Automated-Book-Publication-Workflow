import chromadb
from chromadb.utils import embedding_functions

client = chromadb.Client()
collection = client.get_or_create_collection(name="book_versions")

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

def store_version(doc_id: str, content: str, metadata: dict):
    """
    Stores a final version of the chapter with metadata into ChromaDB.
    """
    collection.add(
        documents=[content],
        ids=[doc_id],
        metadatas=[metadata]
    )


def search_similar_content(query: str, top_k: int = 3):
    """
    Retrieves top-k similar past chapters based on query.
    """
    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )
    return results


def list_all_versions():
    """
    Returns all stored document IDs.
    """
    return collection.get()["ids"]
