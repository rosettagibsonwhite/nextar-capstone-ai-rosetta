from pathlib import Path
import os

from openai import OpenAI


from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)


documents_folder = Path("documents")

documents = []

for file_path in documents_folder.glob("*.txt"):
    text = file_path.read_text(encoding="utf-8")

    documents.append({
        "filename": file_path.name,
        "content": text
    })

print(f"Loaded {len(documents)} documents.")


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = []

for document in documents:

    document_chunks = text_splitter.split_text(
        document["content"]
    )

    for chunk in document_chunks:

        chunks.append({
            "filename": document["filename"],
            "content": chunk
        })

print(f"Created {len(chunks)} chunks.")


print("\nCreating embeddings...")

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding model loaded.")

texts = [chunk["content"] for chunk in chunks]

metadatas = [
    {"source": chunk["filename"]}
    for chunk in chunks
]

vector_store = Chroma.from_texts(
    texts=texts,
    embedding=embedding_model,
    metadatas=metadatas,
    persist_directory="chroma_db"
)

print("Embeddings stored in ChromaDB.")

print("\nRAG knowledge base is ready!")

questions = [
    "How many days of annual leave do NovaTech employees receive?",
    "How many days per week can employees work remotely?",
    "What storage capacity does the standard NovaCloud plan provide?",
    "What are the standard working hours at NovaTech?",
    "What operating systems is NovaNote available on?"
]

for question in questions:

    print("\n" + "=" * 60)
    print("Question:")
    print(question)

    # Retrieve relevant document chunks
    relevant_chunks = vector_store.similarity_search(question, k=3)

    print("\nRelevant information found:")
    for i, result in enumerate(relevant_chunks):
        print(f"\n--- Result {i + 1} ---")
        print(f"Source: {result.metadata['source']}")
        print(result.page_content)

    # Combine retrieved information into context
    context = "\n\n".join(
        result.page_content
        for result in relevant_chunks
    )

    # Generate answer using local Ollama model
    response = client.chat.completions.create(
        model="llama3.2:3b",
        messages=[
            {
                "role": "system",
                "content": (
                    "Answer the question using only the provided context. "
                    "If the answer is not in the context, say you do not "
                    "have enough information."
                )
            },
            {
                "role": "user",
                "content": f"""
Context:
{context}

Question:
{question}
"""
            }
        ]
    )

    print("\nGenerated Answer:")
    print(response.choices[0].message.content)

print("\n" + "=" * 60)
print("All 5 RAG demonstrations completed successfully!")

context = "\n\n".join(
    result.page_content
    for result in relevant_chunks
)

response = client.chat.completions.create(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
            "content": "Answer the question using only the provided context. If the answer is not in the context, say you do not have enough information."
        },
        {
            "role": "user",
            "content": f"""
Context:
{context}

Question:
{question}
"""
        }
    ]
)

print("\nGenerated Answer:")
print(response.choices[0].message.content)