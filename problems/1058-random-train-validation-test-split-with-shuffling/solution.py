import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    # Your code here
    n, d = data.shape
    shuffled_indices = np.random.default_rng(seed).permutation(n)
    shuffled_data = data[shuffled_indices]
    train_end = int(n * train_frac)
    validation_end = train_end + int(n * validation_frac)

    train = shuffled_data[: train_end]
    validation = shuffled_data[train_end : validation_end]
    test = shuffled_data[validation_end :]

    return [train, validation, test]