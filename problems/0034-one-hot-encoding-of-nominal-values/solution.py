import numpy as np

def to_categorical(x, n_col=None):
    # Your code here
    if n_col is None:
        n_col = np.max(x).item() + 1
    
    one_hot_encoding = np.zeros((len(x), n_col))
    for i, element in enumerate(x.tolist()):
        one_hot_encoding[i][element] = 1.0
    
    return one_hot_encoding
