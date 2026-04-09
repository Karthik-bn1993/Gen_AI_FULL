text = """Artificial Intelligence is transforming industries.
Machine learning is a subset of AI.
Deep learning uses neural networks.
Python is widely used for AI development.
It has many libraries like TensorFlow and PyTorch."""

def fixed_chunk(text, chunk_size=50):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

chunks = fixed_chunk(text, chunk_size=60)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")