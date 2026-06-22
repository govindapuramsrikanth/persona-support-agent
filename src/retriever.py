import chromadb


# Create ChromaDB client
client = chromadb.PersistentClient(
    path="vector_db"
)


# Create / Load collection
collection = client.get_or_create_collection(
    name="documents"
)



def retrieve_documents(query):

    try:
        results = collection.query(
            query_texts=[query],
            n_results=3
        )


        documents = results.get("documents", [])


        if documents and len(documents) > 0:
            return documents[0]


        return []


    except Exception as e:

        print("Retriever Error:", e)

        return []