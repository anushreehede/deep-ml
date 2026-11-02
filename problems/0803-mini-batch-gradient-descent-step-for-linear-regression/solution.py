import numpy as np

def mini_batch_gd_step(X: np.ndarray, y: np.ndarray, weights: np.ndarray, bias: float, batch_indices: list, lr: float) -> np.ndarray:
    """
    Perform one mini-batch gradient descent update step for linear regression with MSE loss.
    Returns a 1D array of length D+1: updated weights followed by updated bias.
    """
    
    X_batch = X[batch_indices]
    y_batch = y[batch_indices]
    m = len(batch_indices)

    error = X_batch @ weights + bias - y_batch   # shape (m,)

    grad_w = (2.0 / m) * (X_batch.T @ error)     # shape (D,)
    grad_b = (2.0 / m) * np.sum(error)           # scalar

    new_weights = weights - lr * grad_w          # new array, no mutation
    new_bias = bias - lr * grad_b
    
    return np.append(new_weights, new_bias)
