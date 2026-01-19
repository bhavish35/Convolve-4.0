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

### 2️⃣ Backend
python -m venv vitatrace-env
source vitatrace-env/bin/activate
pip install -r requirements.txt
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

## 🌍 Why VitaTrace?

In real healthcare settings, doctors often face situations like:
- A patient arrives unconscious in an emergency
- Medical history is scattered across hospitals
- X-rays, reports, and doctor notes exist in different formats
- Patients can’t accurately recall their own medical past

Missing or delayed information can lead to wrong decisions, unsafe medication, or delayed treatment.

**VitaTrace** solves this by acting as a **long-term medical memory system** that allows doctors to quickly and safely retrieve relevant patient history across **text, images, and voice notes**.

---

## 🏥 What is VitaTrace?

VitaTrace is a **multimodal healthcare memory assistant** that:

- Stores a patient’s medical history over time
- Understands and searches across different data types
- Provides evidence-based results instead of guesses
- Supports a secure **emergency access mode** for life-saving information

The system is built with **ethics, privacy, and safety** at its core.

---

## ✨ Key Features

### 🧩 Multimodal Medical Memory
VitaTrace works with real medical data formats:

- 📝 Text – lab reports, diagnoses, allergies  
- 🩻 Images – X-rays and scans  
- 🎙️ Audio – doctor voice notes (automatically transcribed)

Each modality uses an AI model designed specifically for that data type.

---

### 🔍 Intelligent Semantic Search
Doctors can ask natural-language questions such as:
- “diabetes risk over time”
- “lung infection x-ray”

The system:
- Searches by **meaning**, not keywords
- Applies similarity confidence thresholds
- Safely returns **“No relevant history found”** when appropriate

This prevents misleading or hallucinated results.

---

### 🚑 Emergency Blind-Access Mode
In emergencies, speed and safety are critical.

Emergency mode:
- Bypasses AI reasoning completely
- Returns only **explicitly marked critical information**
- Shows facts such as:
  - severe allergies
  - life-critical medications
- No inference, no ranking, no guessing

---

### 🧠 Transparent Reasoning
Every response is:
- Backed by retrieved patient records
- Clearly labeled by modality (text / image / audio)
- Written in conservative, clinical language

VitaTrace assists doctors — it never replaces clinical judgment.

---

## 🏗️ How It Works

Doctor / Clinician
↓
FastAPI API
↓
Search & Reasoning Layer
↓
Qdrant Vector Database
↓
Text | Image | Audio Memories


- Each patient record is stored as a vector
- Strict patient-level filtering ensures privacy
- Similarity thresholds ensure relevance

---

## 🧠 AI Models Used

| Purpose | Model |
|------|------|
| Text & Audio Embeddings | all-MiniLM-L6-v2 |
| Image Embeddings | CLIP (ViT-B/32) |
| Audio Transcription | Whisper (base) |
| Vector Database | Qdrant |

All processing runs locally — no external APIs required.

---

## 🧪 Example Queries

| Query | Output |
|----|------|
| diabetes risk over time | Lab trends and diagnoses |
| lung infection x-ray | Chest X-ray and doctor note |
| football | No relevant patient history found |
| Emergency access | Allergies and critical medications |

---

## 🔐 Ethics & Safety

VitaTrace is designed to be responsible by default:

- Strict patient-level access control
- Emergency mode avoids AI inference
- Similarity thresholds prevent false relevance
- Clear separation between facts and interpretation

The system is designed to **fail safely**.

---

