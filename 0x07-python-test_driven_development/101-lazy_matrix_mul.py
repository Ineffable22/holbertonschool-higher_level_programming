#!/usr/bin/python3
"""Lazy matrix multiplication"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices by using the module NumPy"""
    return numpy.matmul(m_a, m_b)
