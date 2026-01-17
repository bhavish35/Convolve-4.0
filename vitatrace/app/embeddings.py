import torch # type: ignore
from sentence_transformers import SentenceTransformer # type: ignore
import clip # type: ignore
from PIL import Image # type: ignore


# Select device for Apple Silicon (M3) or CPU fallback
device = "mps" if torch.backends.mps.is_available() else "cpu"

# Load embedding model once at startup
text_model = SentenceTransformer("all-MiniLM-L6-v2", device=device)

def embed_text(text: str):
    """
    Convert input text into a dense vector embedding
    """
    return text_model.encode(text).tolist()

clip_model, clip_preprocess = clip.load("ViT-B/32", device=device)

def embed_image(image_path: str):
    """
    Convert an image (X-ray, scan) into an embedding vector
    """
    image = Image.open(image_path).convert("RGB")
    image_input = clip_preprocess(image).unsqueeze(0).to(device)

    with torch.no_grad():
        image_features = clip_model.encode_image(image_input)

    return image_features[0].cpu().numpy().tolist()

def embed_clip_text(text: str):
    """
    Convert text into CLIP embedding (for image search)
    """
    text_tokens = clip.tokenize([text]).to(device)

    with torch.no_grad():
        text_features = clip_model.encode_text(text_tokens)

    return text_features[0].cpu().numpy().tolist()



