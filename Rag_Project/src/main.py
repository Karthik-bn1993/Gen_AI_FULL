from ingestion import load_pdf
from chunking import chunk_documents
from embedding import get_embeddings
from vector_store import create_faiss_index
from retriever import retrieve

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

documents = load_pdf("../data/hr_policy.pdf")
chunks = chunk_documents(documents)
texts = [c.page_content for c in chunks]

embeddings = get_embeddings(texts)
index = create_faiss_index(embeddings)

query = input("Ask a question: ")
retrieved = retrieve(query, index, chunks)

context = "\n".join(retrieved)

prompt = f"""Answer ONLY from the context.

Context:
{context}

Question:
{query}
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": prompt}]
)

print("\nAnswer:\n")
print(response.choices[0].message.content)
