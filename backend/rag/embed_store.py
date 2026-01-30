import json
import numpy as np
import faiss
from openai import OpenAI

client = OpenAI()
EMBEDDING_MODEL = "text-embedding-3-small"

def embed_text(text):
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )
    vectors = [d.embedding for d in response.data]
    arr = np.array(vectors, dtype=np.float32)
    faiss.normalize_L2(arr)
    return arr

def build_and_solve_index(chunks, index_path, meta_path):
    vectors = embed_text(chunks)
    dimension = vectors.shape[1]
    index = faiss.IndexFlatIP(dimension)
    index.add(vectors)
    faiss.write_index(index, index_path)

    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump({"chunks": chunks}, f, ensure_ascii=False, indent=2)


def load_index(index_path, meta_path):
    index = faiss.read_index(index_path)
    with open(meta_path, 'r', encoding='utf-8') as f:
        metadata = json.load(f)
    return index, metadata["chunks"]