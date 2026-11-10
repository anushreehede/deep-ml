import numpy as np
from typing import List, Tuple
from itertools import accumulate

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    # Your code here

    indices = list(range(n_samples))
    if shuffle:
        np.random.shuffle(indices)
    
    k_folds = []
    fold_size = int(n_samples / k)
    fold_sizes = [fold_size] * k
    fold_sizes[0] += (n_samples % k)

    ends = list(accumulate(fold_sizes))
    starts = [0] + ends[:-1]
    folds = [indices[s:e] for s, e in zip(starts, ends)]

    split_folds = []
    for i, fold in enumerate(folds):
        test_indices = fold
        train_indices = [y for item in folds[:i] + folds[i+1:] for y in item]
        split_folds.append((train_indices, test_indices))
    
    return split_folds

