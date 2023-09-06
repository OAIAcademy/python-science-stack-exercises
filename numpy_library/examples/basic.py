import numpy as np

# Create a 2D array of zeros
a = np.array((3, 4))

# Print the array
print(a)

# Access an element of the array
print(a[0])

# Modify an element of the array
a[0] = 1.0
print(a)

# Perform arithmetic operations on the array
b = np.array((3, 4))
print(a + b)
print(a * b)
print(np.matmul(a, b))

# Create a 2D numpy matrix with dimensions 3x4
matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(matrix)

# Access the element at row 1, column 2
element = matrix[1, 2]
print(element)

# Transpose the matrix
print(matrix.T)  # Create a 2D numpy matrix with dimensions 4x3

# Multiply the matrices
matrix2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(np.dot(matrix, matrix2))

# max
print(np.max(matrix))
print(np.argmax(matrix))
