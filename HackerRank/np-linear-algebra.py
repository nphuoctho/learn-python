import numpy as np

N = int(input())

A = np.zeros((N, N), dtype=float)

for i in range(N):
    A[i] = list(map(float, input().split()))

print(round(np.linalg.det(A), 2))
