import numpy as np

A = np.array([[1,2,3],
              [0,1,4],
              [5,6,0]])

A_inverse = np.linalg.inv(A)
A1 = np.dot(A, A_inverse)
A2 = np.dot(A_inverse, A)

print("Matrix A is:\n", A)
print("Inverse of matrix A is:\n", A_inverse)
print("A * A_inverse is:\n", A1)
print("A_inverse * A is:\n", A2)
