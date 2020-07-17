import numpy as np


def frobenius_norm(a_matrix):
    '''frobenius norm is used to measure the size of a matrix.
    1. We need to square the marix
    2. We need to get the square root of the sum of the elements in in the matrix
    3. There is another way, computing the norm of the matrix'''
    squared_matrix = np.square(a_matrix)
    Frobenius_norm = np.sqrt(np.sum(squared_matrix))
    return Frobenius_norm

def frobenius_norm_2(a_matrix):
    return np.linalg.norm(a_matrix)