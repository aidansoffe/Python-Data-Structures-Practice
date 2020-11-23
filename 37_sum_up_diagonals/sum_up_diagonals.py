import numpy as np 

def sum_up_diagonals(matrix):
    return sum([matrix[i][i] + matrix[i][-1 - i] for i in range(len(matrix))]) 

print(sum_up_diagonals([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]))