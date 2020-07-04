class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list


    def __str__(self):
        return 'Матрица: \n' + str('\n'.join(['\t'.join([str(column) for column in row]) for row in self.matrix_list]))

    def __add__(self, other):
        new_matrix = [[self.matrix_list[row][column] + other.matrix_list[row][column] for column in
                       range(len(self.matrix_list[0]))] for row in range(len(self.matrix_list))]
        return 'Cумма матриц: \n' + str('\n'.join(['\t'.join([str(column) for column in row]) for row in new_matrix]))


matrix_1 = Matrix([[10, 20, 30], [13, -4, 5], [5, 60, 17], [71, 80, 91]])
matrix_2 = Matrix([[11, 18, 70], [17, 6, 5], [15, 40, 13], [13, 20, -1]])

print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
