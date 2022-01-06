#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
    #new = []
    for row in range(len(matrix)):
        new.append([])
        for col in matrix[row]:
            new[row].append(col ** 2)
    '''
    new = [[col ** 2 for col in row] for row in matrix]
    return new
