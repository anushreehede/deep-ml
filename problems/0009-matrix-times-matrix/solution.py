def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    a_rows = len(a)
    a_columns = len(a[0])
    b_rows = len(b)
    b_columns = len(b[0])

    if a_columns != b_rows:
        return -1
    
    c = []
    n = a_columns
    for i in range(a_rows):
        new_row = []
        for j in range(b_columns):
            new_row.append(sum([a[i][k] * b[k][j] for k in range(n)]))
        c.append(new_row)

    return c