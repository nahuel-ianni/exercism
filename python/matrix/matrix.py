class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(number) for number in substring.split()] for substring in matrix_string.splitlines()]


    def row(self, index):
        """Requests a copy of the values contained on the selected row
        
        Arguments:
            index {int} -- The row number
        
        Returns:
            list -- A copy of the values for the selected row in the matrix
        """

        return self.matrix[index - 1].copy()


    def column(self, index):
        """Requests a copy of the values contained on the selected column
        
        Arguments:
            index {int} -- The column number
        
        Returns:
            list -- A copy of the values for the selected column in the matrix
        """

        return [row[index -1] for row in self.matrix]
        