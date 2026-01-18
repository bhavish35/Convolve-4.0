from fastapi import FastAPI, Query # type: ignore
from app.search import search_memory
from app.reasoning import build_evidence, build_reasoning
from app.search import emergency_access
from app.ingest import store_memory
from fastapi import Body
from fastapi.middleware.cors import CORSMiddleware
from app.embeddings import embed_text
from pydantic import BaseModel

from datetime import datetime, timedelta
import random

OTP_STORE = {}  
# Format:
# {
#   "P001": {
#       "otp": "123456",
#       "expires_at": datetime
#   }
# }

class MemoryRequest(BaseModel):
    patient_id: str
    text: str
    category: str = "clinical"
    critical: bool = False

class EmergencyRequest(BaseModel):
    patient_id: str
    otp: str | None = None

app = FastAPI(
    title="VitaTrace – Multimodal Patient Memory",
    description="Evidence-based healthcare memory & retrieval system",
    version="1.0"
)

#doing this onlu for demo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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


@app.post("/emergency")
def emergency_mode(req: EmergencyRequest):
    """
    Emergency blind-access endpoint.
    """
    # Demo OTP logic
    if req.otp and req.otp != "123456":
        return {"error": "Invalid emergency access code"}

    results = emergency_access(req.patient_id)
    evidence = build_evidence(results)

    return {
        "patient_id": req.patient_id,
        "mode": "emergency",
        "critical_info": evidence,
        "warning": "Emergency access granted and logged"
    }



@app.post("/add_memory")
def add_patient_memory(request: MemoryRequest):
    vector = embed_text(request.text)

    payload = {
        "patient_id": request.patient_id,
        "text": request.text,
        "category": request.category,
        "critical": request.critical
    }

    store_memory(vector=vector, payload=payload)

    return {
        "status": "stored",
        "patient_id": request.patient_id
    }

@app.post("/emergency/request-otp")
def request_emergency_otp(patient_id: str):
    otp = str(random.randint(100000, 999999))
    OTP_STORE[patient_id] = {
        "otp": otp,
        "expires_at": datetime.utcnow() + timedelta(minutes=5)
    }

    # DEMO ONLY — return OTP
    return {
        "patient_id": patient_id,
        "otp": otp,
        "message": "OTP generated (demo only, normally sent via SMS)"
    }

@app.post("/emergency/verify")
def emergency_verify(patient_id: str, otp: str):
    record = OTP_STORE.get(patient_id)

    if not record:
        return {"error": "No OTP requested"}

    if datetime.utcnow() > record["expires_at"]:
        return {"error": "OTP expired"}

    if otp != record["otp"]:
        return {"error": "Invalid OTP"}

    results = emergency_access(patient_id)
    evidence = build_evidence(results)

    return {
        "patient_id": patient_id,
        "mode": "emergency",
        "critical_info": evidence,
        "warning": "Emergency access granted and logged"
    }


