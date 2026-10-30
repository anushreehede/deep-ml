import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    """
    Perform gradient descent optimization.
    
    Args:
        X: Feature matrix of shape (m, n)
        y: Target values of shape (m,)
        weights: Initial weights of shape (n,)
        learning_rate: Step size for gradient descent
        n_epochs: Number of complete passes through the dataset
        batch_size: Size of batches for mini-batch gradient descent (default: 1)
        method: Type of gradient descent ('batch', 'stochastic', or 'mini_batch')
    
    Returns:
        Optimized weights
    """
    # Your code here
    m, n = X.shape
    
    if method == 'batch':
        for epoch in range(n_epochs):
            h = X @ weights
            gradient = 2/m * (X.transpose() @ (h - y))
            weights -= learning_rate * gradient

    if method == 'mini_batch' or method == 'stochastic':
        if method == 'stochastic':
            batch_size = 1
        for epoch in range(n_epochs):
            for i in range(0, m, batch_size):
                start_idx = i
                # Slicing past 'm' cleanly stops at 'm' automatically
                end_idx = min(i + batch_size, m) 
                
                # Dynamic tracking of actual batch size (crucial for the last batch)
                current_batch_size = end_idx - start_idx

                X_batch = X[start_idx:end_idx, :]
                y_batch = y[start_idx:end_idx]
                h_batch = X_batch @ weights
                gradient = 2/current_batch_size * (X_batch.transpose() @ (h_batch - y_batch))
                weights -= learning_rate * gradient

    return weights.flatten()
