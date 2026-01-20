from qdrant_client import QdrantClient 
from qdrant_client.models import VectorParams, Distance 

client = QdrantClient("localhost", port=6333) 

collections = { "patient_text_memory": 384, 
               "patient_image_memory": 512, 
               "patient_audio_memory": 384, 
              } 

for name, size in collections.items(): 
  client.create_collection( collection_name=name,
                           vectors_config=VectorParams(size=size,  distance=Distance.COSINE) 
                          ) 
  print(f"Created {name}")
