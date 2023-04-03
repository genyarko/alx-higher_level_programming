#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a matrix multiplication function using NumPy."""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    # convert input matrices to NumPy arrays
    a = np.array(m_a)
    b = np.array(m_b)
    
    # perform matrix multiplication using NumPy's dot() function
    result = np.dot(a, b)
    
    # convert result back to a list of lists
    return result.tolist()
