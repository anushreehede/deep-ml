import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    # Your code here
    n, d = X.shape
    for i in range(0, n, batch_size):
        if i + batch_size > n:
            X_batch = X[i: n]
        else:
            X_batch = X[i: i+batch_size]
        if y is not None:
            if i + batch_size > n:
                y_batch = y[i: n]
            else:
                y_batch = y[i: i+batch_size]
            yield (X_batch, y_batch)
        else:
            yield X_batch