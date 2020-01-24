def saddle_points(matrix):
    if not matrix:
        return []

    if len(set([len(row) for row in matrix])) > 1:
        raise ValueError("Irregular matrices are not supported.")

    transposed_matrix = _transpose_matrix(matrix)
    indexes_row_max = []
    indexes_col_min = []

    for index, row in enumerate(matrix):
        indexes_row_max.append([_format_saddle_point(index, i) for i, v in enumerate(row) if v == max(row)])

    for index, column in enumerate(transposed_matrix):
        indexes_col_min.append([_format_saddle_point(i, index) for i, v in enumerate(column) if v == min(column)])

    flattened_indexes_row = [item for sublist in indexes_row_max for item in sublist]
    flattened_indexes_col = [item for sublist in indexes_col_min for item in sublist]

    return [value for value in flattened_indexes_row if value in flattened_indexes_col]


def _transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def _format_saddle_point(row, column):
    return {"row": row + 1, "column": column + 1}
