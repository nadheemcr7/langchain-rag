import argparse
# from dataclasses import dataclass
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

CHROMA_PATH = "chroma"


def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text

    # Prepare the DB with HuggingFace embeddings
    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    if len(results) == 0 or results[0][1] < 0.5:  # Lowered threshold for better matches
        print(f"Unable to find matching results.")
        return

    print("\nRelevant passages from Alice in Wonderland:\n")
    for doc, score in results:
        print(f"Relevance: {score:.3f}")
        print(f"Content: {doc.page_content}\n")


if __name__ == "__main__":
    main()
