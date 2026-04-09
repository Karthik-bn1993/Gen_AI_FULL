import numpy as np
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def get_query_embedding(query):
    res = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    )
    return np.array(res.data[0].embedding).astype("float32")

def retrieve(query, index, chunks, top_k=3):
    q_emb = get_query_embedding(query)
    D, I = index.search(np.array([q_emb]), top_k)
    return [chunks[i].page_content for i in I[0]]
