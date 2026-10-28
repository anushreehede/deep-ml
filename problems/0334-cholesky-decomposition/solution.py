import numpy as np

def cholesky_decomposition(A):
    """
    Perform Cholesky decomposition on a symmetric positive-definite matrix.
    
    Args:
        A: A symmetric positive-definite matrix (2D list or numpy array)
    
    Returns:
        L: Lower triangular matrix such that A = L @ L.T as a 2D list,
           or -1 if decomposition is not possible
    """
    # Your code here
    A = np.array(A)
    if len(A.shape) !=2 or A.shape[0] != A.shape[1]:
        return -1

    n = A.shape[0]
    L = np.zeros_like(A)

    for j in range(n):
        diagonal = A[j, j] - L[j, :j] @ L[j, :j]

        if diagonal <= 0:
            return -1

        L[j, j] = np.sqrt(diagonal)

        for i in range(j + 1, n):
            L[i, j] = (
                A[i, j] - L[i, :j] @ L[j, :j]
            ) / L[j, j]

    return L.tolist()

    