import numpy as np

n, m, p = map(int, input().split())

arr1 = np.array([input().split() for _ in range(n)], int)
arr2 = np.array([input().split() for _ in range(m)], int)

res = np.concatenate((arr1, arr2), axis=0)
print(res)
