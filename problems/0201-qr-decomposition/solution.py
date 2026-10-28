import numpy as np

def qr_decomposition(A: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
	"""
	Perform QR decomposition using Gram-Schmidt process.
	
	Args:
		A: An m x n matrix represented as list of lists
	
	Returns:
		Tuple of (Q, R) where Q is orthogonal and R is upper triangular
	"""
	# Your code here
	A = np.asarray(A, dtype=float)
	m, n = A.shape
	if m < n:
		raise ValueError("This implementation requires rows >= columns.")

	Q = np.zeros((m, n))
	R = np.zeros((n, n))

	for j in range(n):
		v = A[:, j].copy()

		# Remove projections onto previous columns of Q.
		for i in range(j):
			R[i, j] = Q[:, i] @ v
			v -= R[i, j] * Q[:, i]

		# Normalize the remaining vector.
		R[j, j] = np.linalg.norm(v)

		Q[:, j] = v / R[j, j]

	return Q, R