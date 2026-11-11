import numpy as np

def ordinal_encode(X, categories):
    """
    Encode categorical features as integer codes using a provided ordering.

    Args:
        X: 2D list/array of shape (n_samples, n_features) with string values.
        categories: list of length n_features; categories[j] is an ordered
                    list of valid categories for column j.

    Returns:
        np.ndarray of shape (n_samples, n_features), dtype int.
        Unknown categories are encoded as -1.
    """
    categories_dict = [{word: i for i, word in enumerate(category)} for category in categories]

    ordinal_encoding = []
    for row in X:
        encoding = []
        for i, item in enumerate(row):
            if item in categories[i]:
                encoding.append(categories_dict[i][item])
            else:
                encoding.append(-1)
        ordinal_encoding.append(encoding)
    
    return np.array(ordinal_encoding)
