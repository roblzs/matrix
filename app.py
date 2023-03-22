import numpy as np

A = np.array([
    [2, 3, 1],
    [-1, 2, 4],
    [5, 3, 0]
])

B = np.array([
    [2, 7, 13],
    [-1, 0, 5],
    [5, 13, 21]
])

aSqr = A * A
aSqrSub = aSqr - B

aSqrSubMul = A * aSqrSub

bPa = B + A

bPaTb = bPa * B

bPaTbT2 = 2 * bPaTb

result = aSqrSubMul - bPaTbT2

print(result)