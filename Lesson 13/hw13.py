import numpy as np

# 1. Create a vector with values ranging from 10 to 49
v1 = np.arange(10, 50)

# 2. Create a 3x3 matrix with values ranging from 0 to 8
m1 = np.arange(9).reshape(3, 3)

# 3. Create a 3x3 identity matrix
identity = np.eye(3)

# 4. Create a 3x3x3 array with random values
arr3d = np.random.rand(3, 3, 3)

# 5. Create a 10x10 array with random values and find min & max
arr10 = np.random.rand(10, 10)
min_val = arr10.min()
max_val = arr10.max()

# 6. Create a random vector of size 30 and find the mean
v30 = np.random.rand(30)
mean_v30 = v30.mean()

# 7. Normalize a 5x5 random matrix
m5 = np.random.rand(5, 5)
normalized_m5 = (m5 - m5.min()) / (m5.max() - m5.min())

# 8. Multiply a 5x3 matrix by a 3x2 matrix
A = np.random.rand(5, 3)
B = np.random.rand(3, 2)
product_5x3_3x2 = A @ B

# 9. Create two 3x3 matrices and compute dot product
m2 = np.random.rand(3, 3)
m3 = np.random.rand(3, 3)
dot_product = np.dot(m2, m3)

# 10. Given a 4x4 matrix, find its transpose
m4 = np.random.rand(4, 4)
transpose_m4 = m4.T

# 11. Create a 3x3 matrix and calculate determinant
m_det = np.random.rand(3, 3)
determinant = np.linalg.det(m_det)

# 12. Create A (3x4) and B (4x3) and compute A·B
A2 = np.random.rand(3, 4)
B2 = np.random.rand(4, 3)
product_A2_B2 = A2 @ B2

# 13. Matrix-vector product (3x3 matrix and 3x1 vector)
m_vec = np.random.rand(3, 3)
vec = np.random.rand(3, 1)
matrix_vector_product = m_vec @ vec

# 14. Solve Ax = b (A is 3x3, b is 3x1)
A3 = np.random.rand(3, 3)
b = np.random.rand(3, 1)
x = np.linalg.solve(A3, b)

# 15. Row-wise and column-wise sums of a 5x5 matrix
m_sum = np.random.rand(5, 5)
row_sums = m_sum.sum(axis=1)
col_sums = m_sum.sum(axis=0)