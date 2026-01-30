@app.post("/ingest")
def ingest():
    global index, chunks
    text = pdf_to_text(PDF_PATH)
    chunks = chunk_text(text)
    build_and_save_index(chunks, INDEX_PATH, META_PATH)
    index, chunks = load_index(INDEX_PATH, META_PATH)
    return {"status": "ok", "chunks": len(chunks)}

@app.post("/chat")
def chat(payload: chatIn):
    global index, chunks
    if index is None or chunks is None:
        if os.path.exists(INDEX_PATH) and os.path.exists(META_PATH):
            index, chunks = load_index(INDEX_PATH, META_PATH)
        else:
            return {"answer": "Knowlege base not ingested yet."}
    
    hits = retrieve(payload.message, index, chunks)
    answer = generate_answer(payload.message, hits)
    return {"answer": answer}