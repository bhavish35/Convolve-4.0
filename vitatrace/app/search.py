from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue

from app.embeddings import (
    embed_text,
    embed_clip_text
)

client = QdrantClient("localhost", port=6333)

# Similarity threshold (important!)
SIMILARITY_THRESHOLD = 0.1


def _patient_filter(patient_id: str):
    return Filter(
        must=[
            FieldCondition(
                key="patient_id",
                match=MatchValue(value=patient_id)
            )
        ]
    )


def _filter_by_score(results):
    return [r for r in results if r.score >= SIMILARITY_THRESHOLD]


# ----------------------------
# NORMAL MULTIMODAL SEARCH
# ----------------------------
def search_memory(query: str, patient_id: str, limit: int = 5):
    """
    Unified multimodal semantic search
    (text + audio + image)
    """

    # --- TEXT SEARCH ---
    text_vec = embed_text(query)
    raw_text = client.search(
        collection_name="patient_text_memory",
        query_vector=text_vec,
        query_filter=_patient_filter(patient_id),
        limit=limit
    )
    text_results = _filter_by_score(raw_text)

    # --- AUDIO SEARCH ---
    raw_audio = client.search(
        collection_name="patient_audio_memory",
        query_vector=text_vec,
        query_filter=_patient_filter(patient_id),
        limit=limit
    )
    audio_results = _filter_by_score(raw_audio)

    # --- IMAGE SEARCH (CLIP) ---
    image_vec = embed_clip_text(query)
    raw_images = client.search(
        collection_name="patient_image_memory",
        query_vector=image_vec,
        query_filter=_patient_filter(patient_id),
        limit=limit
    )
    image_results = _filter_by_score(raw_images)

    return {
        "text": text_results,
        "audio": audio_results,
        "image": image_results
    }


# ----------------------------
# EMERGENCY BLIND ACCESS
# ----------------------------
def emergency_access(patient_id: str, limit: int = 5):
    """
    Emergency mode:
    - NO semantic search
    - ONLY metadata filtering
    - ONLY critical records
    """

    return client.scroll(
        collection_name="patient_text_memory",
        scroll_filter=Filter(
            must=[
                FieldCondition(
                    key="patient_id",
                    match=MatchValue(value=patient_id)
                ),
                FieldCondition(
                    key="critical",
                    match=MatchValue(value=True)
                )
            ]
        ),
        limit=limit
    )[0]
