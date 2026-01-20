# 🧠 VitaTrace  
### A Multimodal Patient Memory System for Safer, Smarter Healthcare

---

### 🔧 Tech Stack
- FastAPI (Backend)
- Qdrant (Vector DB)
- SentenceTransformers
- React + Vite (Frontend)

---

## 🚀 How to Run 

### 1️⃣ Start Qdrant
```bash
docker run -p 6333:6333 qdrant/qdrant
```
### 2️⃣ Backend
```bash
python -m venv vitatrace-env
source vitatrace-env/bin/activate
pip install -r requirements.txt

cd vitatrace/app
python3 create_collections.py

cd ..
uvicorn app.api:app --reload

```
Backend: http://127.0.0.1:8000  
Swagger: http://127.0.0.1:8000/docs

### 3️⃣ Frontend
```bash
cd frontend
npm install
npm run dev
```

Frontend: http://localhost:5173

---
### Template to store audio in vectorbase
```bash
python - << 'EOF'
from app.audio import transcribe_audio
from app.embeddings import embed_text
from app.ingest import store_memory

text = transcribe_audio("audio_path")
vec = embed_text(text)

store_memory(
    vec,
    payload={
        "patient_id": "P001",
        "modality": "audio",
        "category": "emergency_note",
        "date": "2024-01-18",
        "summary": text[:200],
        "critical": True
    },patient_audio_memory
)
EOF
```

### Template to store image in vectorbase
```bash
python - << 'EOF'
from app.embeddings import embed_image
from app.ingest import store_memory

# Step 1: Embed image
vec = embed_image("data/xrays/chest_xray_001.jpg")

# Step 2: Store in patient memory
store_memory(
    vec,
    payload={
        "patient_id": "P001",
        "modality": "image",
        "category": "xray",
        "date": "2024-01-15",
        "summary": "Chest X-ray indicating possible lung infection",
        "critical": False
    },patient_image_memory
)

print("Image memory stored successfully")
EOF

```

---
```text
For text memory you can go to frontend

I have done it in frontend just for demo
```
---

