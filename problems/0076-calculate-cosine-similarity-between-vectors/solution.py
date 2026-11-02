import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	dot = np.dot(v1, v2)

	l2_norm_v1 = np.linalg.norm(v1, ord=2)
	l2_norm_v2 = np.linalg.norm(v2, ord=2)

	similarity = dot / (l2_norm_v1 * l2_norm_v2)

	return similarity
	
