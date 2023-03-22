import numpy as np


A = np.array([
    [4, 5, -2],
    [3, -1, 0],
    [4, 2, 7]
])

B = np.array([
    [2, 1, -1],
    [0, 1, 2],
    [5, 7, 3]
])
# print(A * np.linalg.inv(A))
# print(np.linalg.det(A))
# print(np.linalg.(A) / np.linalg.det(A))
print(np.matmul(np.linalg.inv(A), B))

