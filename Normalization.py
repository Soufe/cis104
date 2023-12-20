import numpy as np
def normalization(A):
    row_sums = A.sum(axis=1, keepdims=True)
    normalized_A = A / row_sums
    return normalized_A