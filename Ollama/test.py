import ollama

response = ollama.chat(
    model="llama3",
    messages=[
        {"role": "user", "content": "What is AI?"}
    ]
)

print(response['message']['content'])

# ollama pull nomic-embed-text
