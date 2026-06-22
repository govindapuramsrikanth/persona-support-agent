from pathlib import Path


def load_documents():
    """
    Reads all markdown files from data folder
    and returns their content
    """

    documents = []

    data_path = Path("data")


    for file in data_path.glob("*.md"):

        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

            documents.append({
                "file_name": file.name,
                "content": content
            })


    return documents



if __name__ == "__main__":

    docs = load_documents()

    for doc in docs:
        print("FILE:", doc["file_name"])
        print(doc["content"])