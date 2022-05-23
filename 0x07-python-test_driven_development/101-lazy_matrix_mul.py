#!/usr/bin/python3
"""
Lazy matrix multiplication
multiply two matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    '''
      Multiplies 2 matrices
        m_a : first matrix
        m_b : second matrix
    '''
    return np.matmul(m_a, m_b)