import tiktoken

def chunk_text(text, chunk_size=200, overlap=50):
    enc = tiktoken.encoding_for_model("gpt-4o-mini")
    tokens = enc.encode(text)    # "hello world"  ="1231, 86941"  text to ID(Binary data)
    

    chunks = []
    for i in range(0, len(tokens), chunk_size - overlap):
        chunk = tokens[i:i + chunk_size]
        chunks.append(enc.decode(chunk))

    return chunks


# def chunk_documents(documents, chunk_size=200, overlap=50):
#     import tiktoken

#     enc = tiktoken.encoding_for_model("gpt-4o-mini")

#     chunks = []

#     for doc in documents:
#         tokens = enc.encode(doc["text"])

#         for i in range(0, len(tokens), chunk_size - overlap):
#             chunk_tokens = tokens[i:i + chunk_size]
#             chunk_text = enc.decode(chunk_tokens)

#             chunks.append({
#                 "text": chunk_text,
#                 "source": doc["source"],
#                 "page": doc["page"]
#             })

#     return chunks