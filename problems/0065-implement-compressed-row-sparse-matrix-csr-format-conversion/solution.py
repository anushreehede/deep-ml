import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	values_array = []
	column_indices = []
	row_pointers = [0]
	cumulative = 0
	m, n = len(dense_matrix), len(dense_matrix[0])
	for i in range(m):
		for j in range(n):
			if dense_matrix[i][j] != 0:
				values_array.append(dense_matrix[i][j])
				cumulative += 1
				column_indices.append(j)
		row_pointers.append(cumulative)

	return (values_array, column_indices, row_pointers)
