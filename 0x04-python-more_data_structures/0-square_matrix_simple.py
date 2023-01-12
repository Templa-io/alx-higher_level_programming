def square_matrix_simple(matrix=[]):
	return list(map(lambda row: list(map(lambda elem:elem**2, row)), matrix))
