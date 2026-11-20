import numpy as np
from scipy import stats

def impute_missing_data(data: np.ndarray, strategy: str = 'mean') -> np.ndarray:
    """
    Impute missing values in a 2D array using the specified strategy.
    
    Args:
        data: 2D numpy array with missing values represented as np.nan
        strategy: Imputation strategy - 'mean', 'median', or 'mode'
        
    Returns:
        2D numpy array with missing values imputed
    """
    # Your code here
    if strategy == 'mean':
        mean = np.nanmean(data, axis=0)
        data = np.where(np.isnan(data), mean, data)
    elif strategy == 'median':
        median = np.nanmedian(data, axis=0)
        data = np.where(np.isnan(data), median, data)
    elif strategy == 'mode':
        result = stats.mode(data, axis=0, keepdims=False)
        mode = result.mode
        data = np.where(np.isnan(data), mode, data)
    
    return data