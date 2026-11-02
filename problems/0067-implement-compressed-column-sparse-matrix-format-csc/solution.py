def compressed_col_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix into its Compressed Column Sparse (CSC) representation.

	:param dense_matrix: List of lists representing the dense matrix
	:return: Tuple of (values, row indices, column pointer)
	"""
	m, n = len(dense_matrix), len(dense_matrix[0])
	values = []
	row_indices = []
	column_pointer = [0]
	cumulative = 0
	for i in range(n):
		for j in range(m):
			if dense_matrix[j][i] != 0:
				values.append(dense_matrix[j][i])
				row_indices.append(j)
				cumulative += 1
		column_pointer.append(cumulative)
	
	return (values, row_indices, column_pointer)

