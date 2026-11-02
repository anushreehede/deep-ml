import numpy as np

def pairwise_cosine_similarity(X):
    # Your code here
    X = np.array(X)
    n, d = X.shape
    similarity_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            norm_i = np.linalg.norm(X[i])
            norm_j = np.linalg.norm(X[j])
            sim = np.dot(X[i], X[j]) / (norm_i * norm_j) if (norm_i != 0 and norm_j != 0) else 0
            similarity_matrix[i][j] = np.round(sim, 4)
    
    return similarity_matrix.tolist()

