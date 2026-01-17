from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
import uuid

# Connect to local Qdrant
client = QdrantClient("localhost", port=6333)

def init_collection():
    """
    Create the patient_memory collection if it does not exist
    """
    collections = client.get_collections().collections
    if "patient_memory" not in [c.name for c in collections]:
        client.create_collection(
            collection_name="patient_memory",
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )
        print("Created collection: patient_memory")
    else:
        print("Collection already exists")

def store_memory(vector, payload, collection_name="patient_text_memory"):
    client.upsert(
        collection_name=collection_name,
        points=[
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload=payload
            )
        ]
    )

