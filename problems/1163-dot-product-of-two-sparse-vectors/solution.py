def sparse_dot_product(vec1, vec2):
    # vec1 and vec2 are lists of numbers of equal length
    # return their dot product
    dot_product = 0
    for (i, j) in zip(vec1, vec2):
        if i != 0 and j != 0:
            dot_product += (i *j)
    return dot_product