def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    rows = len(a)
    columns = len(a[0])
    
    transpose = []
    for col in range(columns):
        new_row = []
        for row in a:
            new_row.append(row[col])
        transpose.append(new_row)
    
    return transpose