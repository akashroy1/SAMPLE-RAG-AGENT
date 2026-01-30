import tiktoken

def chunk_text(text, size=450, overlap=80):
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)

    chunks, start = [], 0
    while start < len(tokens):
        end = start + size
        chunk = tokens[start:end]
        chunks.append(enc.decode(chunk))
        start += size - overlap
    return chunks