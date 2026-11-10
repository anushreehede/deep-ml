import numpy as np

def shuffle_data(X, y, seed=None):
    # Your code here
    n, d = X.shape
    if seed is not None:
        np.random.seed(seed)
    shuffled_indices = np.random.permutation(n)
    shuffled_X = X[shuffled_indices]
    shuffled_y = y[shuffled_indices]

    return (shuffled_X, shuffled_y)