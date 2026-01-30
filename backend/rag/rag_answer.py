def retrieve(query, index, chunks, k=4):
    qvec = embed_texts([query])
    _, ids = index.search(qvec, k)
    return [chunks[i] for i in ids[0] if i != -1]

def generate_answer(q, ctx):
    context = "\n".join(ctx)
    res = client.responses.create(
        model="gpt-5.2",
        instructions="Use only the context.",
        input=f"{context}\n\nQuestion: {q}"
    )

    return res.output_text