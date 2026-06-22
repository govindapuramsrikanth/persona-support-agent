import chromadb
from sentence_transformers import SentenceTransformer

from src.document_loader import load_documents


# Load embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# Create Chroma database
client = chromadb.PersistentClient(
    path="vector_db"
)


collection = client.get_or_create_collection(
    name="support_docs"
)



def create_vector_database():

    documents = load_documents()


    for index, doc in enumerate(documents):

        embedding = model.encode(
            doc["content"]
        ).tolist()


        collection.add(
            ids=[str(index)], 
            embeddings=[embedding],
            documents=[doc["content"]],
            metadatas=[
                {
                    "source": doc["file_name"]
                }
            ]
        )


    print("Vector Database Created Successfully")


def retrieve_documents(query):

    query_embedding = model.encode(
        query
    ).tolist()


    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )


    return results["documents"][0] 




if __name__ == "__main__":

    answer = retrieve_documents(
        "How many days do I have for refund?"
    )

    print(answer)