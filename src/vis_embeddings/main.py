from vis_embeddings.SAMPLE_PAPER_ABSTRACTS import papers
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

def main():
    print(f"Loaded {len(papers)} papers.")

    # Generate embeddings
    model = SentenceTransformer('all-miniLM-L6-v2')

    abstracts = [paper['abstract'] for paper in papers]
    embeddings = model.encode(abstracts)

    print("\n")
    print("-" * 50)
    print(f"Shape of 'embeddings': {embeddings.shape}")
    print(f"Datatype of 'embeddings': {type(embeddings)}")
    print(f"Each abstract is a {embeddings.shape[1]}-dimensional vector")
    print(f"\nFrist few values of the first embedding: {embeddings[0][:15]}")

    # Dimensionality reduction with PCA
    pca = PCA(n_components=2)
    embeddings_2d = pca.fit_transform(embeddings)

    print(f"\nOriginal embedding dimensions: {embeddings.shape[1]}")
    print(f"Reduced embedding dimensions: {embeddings_2d.shape[1]}")
    print(f"Variance explained by these two dimensions: {pca.explained_variance_ratio_.sum():.2%}")

    # Visualize 2d embeddings
    for (x, y) in embeddings_2d:
        plt.scatter(x, y)

    plt.xlabel('First Principal Component')
    plt.ylabel('Second Pricipal Component')
    plt.title('Embeddings')

    plt.show()


if __name__ == "__main__":
    main()
