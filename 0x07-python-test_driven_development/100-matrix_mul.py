#!/user/bin/python3
"""Defines a matrix multiplication function."""

def matrix_mul(m_a, m_b):
    """"Multiplies two Matrices.

    Args:
        m_a (list of listd of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a, m_b is not lists of lists of ints/floats.
        TypeError: If either m_a, m_b have diff sized rows.
        TypeError: if either m_a, m_b is empty.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
            for ele in [num for row in m_a for num in row]):
