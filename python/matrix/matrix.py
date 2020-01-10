class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []

        for substring in matrix_string.splitlines():
            converted_line = list(map(int, substring.split()))

            self.matrix.append(converted_line)


    def row(self, index):
        return self.matrix[index - 1]


    def column(self, index):
        column = []

        for row in self.matrix:
            column.append(row[index - 1])
        
        return column