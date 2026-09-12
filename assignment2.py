# 1. Create following two vectors (one dimensional array)


# a) Vector as a row vector.
import numpy as np

row_vector = np.array([20, 50, 1, 10])
print("Row Vector:\n", row_vector)

col_vector = np.array([[10], [20], [30], [40]])
print("\nColumn Vector:\n", col_vector)


# 2. Create following matrices (two dimensional arrays)

# a) matrix with three rows and two columns.

mat_3x2 = np.array([[1, 2], [3, 4], [5, 6]])
print("3x2 Matrix:\n", mat_3x2)

mat_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n3x3 Matrix:\n", mat_3x3)

mat_4x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print("\n4x3 Matrix:\n", mat_4x3)

# 3. Display first element, last element and second element of any vector.

my_vector = np.array([60, 75, 80, 95, 100])
print("Vector:", my_vector)
print("First element:", my_vector[0])
print("Last element:", my_vector[-1])
print("Second element:", my_vector[1])

# 4. a) Display first row of the any matrix.
# b) Display second column of the any matrix
f_mat = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print("matrix :n", f_mat)
print("\na) First row:", f_mat[0, :])
print("b) Second column:", f_mat[:, 1])


# 5. Create any one matrix and describe following details.
# a) number of rows and columns
# b)number of rows only
# c) number of elements (size)
# d) dimensions


info_mat = np.zeros((4, 5))
print("Matrix created: 4x5 of zeros")
print("a) Number of rows and columns:", info_mat.shape)
print("b) Number of rows only:", info_mat.shape[0])
print("c) Number of elements (size):", info_mat.size)
print("d) Dimensions:", info_mat.ndim)
