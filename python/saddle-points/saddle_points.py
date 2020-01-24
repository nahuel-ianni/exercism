def saddle_points(matrix):
    if len(set([len(row) for row in matrix])) > 1:
        raise ValueError("Irregular matrices are not supported.")

    inverted_matrix = _invert_matrix(matrix)
    indexes_row_max = []
    indexes_col_min = []

    for index, row in enumerate(matrix):
        indexes_row_max.append([_format_saddle_point(index, i) for i, v in enumerate(row) if v == max(row)])

    for index, column in enumerate(inverted_matrix):
        indexes_col_min.append([_format_saddle_point(i, index) for i, v in enumerate(column) if v == min(column)])

    print(indexes_row_max)
    print(indexes_col_min)
    print("-------------")

    flattened_indexes_row = [item for sublist in indexes_row_max for item in sublist]
    flattened_indexes_col = [item for sublist in indexes_col_min for item in sublist]

    print(flattened_indexes_row)
    print(flattened_indexes_col)
    print("-------------")

    saddle_points = [value for value in flattened_indexes_row if value in flattened_indexes_col] # list(set(flattened_indexes_row) & set(flattened_indexes_col)) #

    print(saddle_points)
    print("-------------")

    return saddle_points


    #=====================================================================================
    # for index, row in enumerate(matrix):
    #     for column in inverted_matrix:
    #         indexes_row_min = [i for i, v in enumerate(row) if v == max(row)]
    #         indexes_col_max = [i for i, v in enumerate(column) if v == min(column)]#enumerate(max(column))

    #         if indexes_col_max == indexes_row_min:
    #             saddle_points.append(indexes_row_min)
    #=====================================================================================


def _invert_matrix(matrix):
    inverted_matrix = []
    index = 0

    for row in matrix:
        inverted_matrix.append([row[index] for row in matrix])
        index += 1

    return inverted_matrix


def _format_saddle_point(row, column):
    return {"row": row + 1, "column": column + 1}
