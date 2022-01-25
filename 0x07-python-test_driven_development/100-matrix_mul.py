#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == []:
        raise ValueError("m_a can't be empty")
    if 0 in list(map(lambda arr: len(arr), m_a)):
        raise ValueError("m_a can't be empty")
    if m_b == []:
        raise ValueError("m_b can't be empty")
    for i in m_b:
        if i == []:
            raise ValueError("m_b can't be empty")
	
    for i in m_a:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        for j in i:
            if type(j) not in [float, int]:
                raise TypeError("m_b should contain only integers or floats")
	
    for sub_list in m_a:
        if len(m_a[0]) != len(sub_list):
            raise TypeError("each row of m_a must be of the same size")

    for sub_list in m_b:
        if len(m_b[0]) != len(sub_list):
            raise TypeError("each row of m_b must be of the same size")
	
    col_a = len(m_a[0])
    row_b = len(m_b)
    if col_a != row_b:
        raise ValueError("m_a and m_b can't be multiplied")

    n_row = len(m_a)
    n_col = len(m_b[0])
    
    i = 0
    j = 0
    mtx = []
    result = 0
    for col in range(n_col):
        """row[0]* m_b(col[0])"""
        
        for row in range(n_row):
            mtx.append([])
            result = 0
            for _row in range(len(m_a[0])):
               result += m_a[row][_row] * m_b[_row][col]
            mtx[row].append(result)
        """
        [[1, 2], [3, 4]], [[1, 2], [3, 4]]
        [0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0] = 7
        [0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1] = 10
        [1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0] = 15
        [1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1] = 22
        """
    mtx = list(filter(lambda arr: len(arr) != 0, mtx))
    return mtx
