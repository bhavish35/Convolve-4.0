from fastapi import FastAPI, Query # type: ignore
from app.search import search_memory
from app.reasoning import build_evidence, build_reasoning
from app.search import emergency_access


app = FastAPI(
    title="VitaTrace – Multimodal Patient Memory",
    description="Evidence-based healthcare memory & retrieval system",
    version="1.0"
)

@app.get("/")
def root():
    return {
        "message": "VitaTrace API is running",
        "status": "ok"
    }

@app.get("/query")
def query_patient(
    patient_id: str = Query(..., description="Patient ID"),
    query: str = Query(..., description="Doctor query")
):
    """
    Query patient memory and return evidence-based reasoning
    """

    # 1. Search patient memory
    results = search_memory(query=query, patient_id=patient_id)

    # 2. Build evidence
    evidence = build_evidence(results)

    # 3. Build reasoning
    reasoning = build_reasoning(query, evidence)

    return {
        "patient_id": patient_id,
        "query": query,
        "evidence": evidence,
        "reasoning": reasoning
    }


@app.get("/emergency")
def emergency_mode(
    patient_id: str,
    otp: str
):
    """
    Emergency blind-access endpoint.
    OTP is simulated for demo purposes.
    """
    if otp != "123456":
        return {"error": "Invalid emergency access code"}

    results = emergency_access(patient_id)
    evidence = build_evidence(results)

    return {
        "patient_id": patient_id,
        "mode": "emergency",
        "critical_info": evidence,
        "warning": "Emergency access granted and logged"
    }
