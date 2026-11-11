from vis_embeddings.SAMPLE_PAPER_ABSTRACTS import papers
from sentence_transformers import SentenceTransformer

def main():
    print(f"Loaded {len(papers)} papers.")

    # Generate vis_embeddings
    model = SentenceTransformer('all-miniLM-L6-v2')

    abstracts = [paper['abstract'] for paper in papers]
    embeddings = model.encode(abstracts)

    print("\n")
    print("-" * 50)
    print(f"Shape of 'embeddings': {embeddings.shape}")
    print(f"Datatype of 'embeddings': {type(embeddings)}")
    print(f"Each abstract is a {embeddings.shape[1]}-dimensional vector")
    print(f"\nFrist few values of the first embedding: {embeddings[0][:15]}")

if __name__ == "__main__":
    main()
