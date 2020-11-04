import numpy as np
A1 = [[5, 19, 3], 
      [2,-11,25], 
      [10,6,-1]]

A2 = [[7, -6, 7],
      [27,31,-5], 
      [-7,30,1]]

A3  = [[0,0,0],
       [0,0,0],
       [0,0,0]]
matrix_length = len(A1)
for i in range(len(A1)):
    for j in range(len(A2)):
            A3[i][j] = A1[i][j] + A2[i][j]

print("Sum of Matrix A1 and A2 = ", A3)
for i in range(len(A1)):
    for j in range(len(A2)):
            A3[i][j] = A1[i][j] * A2[i][j]

print("Multiplication of Matrix A1 and A2 = ", A3)
A1 = np.array([[13, 26, 5], [4, 0, 3], [12,-19,22]])
A2 = A1.transpose()

print(A2)
