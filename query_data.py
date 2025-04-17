import argparse
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

CHROMA_PATH = "chroma"

def main():
    # Create CLI
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text

    # Prepare the DB
    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB
    results = db.similarity_search_with_relevance_scores(query_text, k=5)
    if len(results) == 0:
        print("Unable to find matching results.")
        return

    print(f"Relevant passages from the document:\n")
    for doc, score in results:
        # Normalize score to 0-1 range if negative
        normalized_score = max(0, min(1, score))
        if normalized_score > 0.0:
            print(f"Source: {doc.metadata['source']}")
            print(f"Relevance: {normalized_score:.3f}")
            print(f"Content: {doc.page_content}\n")

if __name__ == "__main__":
    main()