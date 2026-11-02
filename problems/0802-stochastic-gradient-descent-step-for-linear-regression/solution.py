import numpy as np

def sgd_update(X: np.ndarray, y: np.ndarray, weights: np.ndarray, learning_rate: float, n_iter: int) -> list:
    """
    Perform n_iter steps of stochastic gradient descent on a linear regression
    model with MSE loss, cycling through samples in order.

    Returns the final weight vector as a Python list.
    """
    m, n = X.shape

    for epoch in range(n_iter):
        idx = epoch % m
        X_batch = X[idx]
        y_batch = y[idx]
        h_batch = X_batch @ weights
        gradient = 2 * (X_batch.transpose() * (h_batch - y_batch))
        weights -= learning_rate * gradient
    
    return weights.flatten()
