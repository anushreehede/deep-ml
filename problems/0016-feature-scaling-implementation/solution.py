import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # Your code here
    mean = np.mean(data, axis=0)
    std_dev = np.std(data, axis=0)
    max_val = np.max(data, axis=0)
    min_val = np.min(data, axis=0)
    standardized_data = np.round(((data - mean) / std_dev), 4)
    normalized_data = np.round(((data - min_val) / (max_val - min_val)), 4)
    return standardized_data, normalized_data