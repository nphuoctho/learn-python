from collections import defaultdict

n, m = list(map(int, input().split()))

A = defaultdict(list)

for i in range(n):
    A[input()].append(i + 1)

for i in range(m):
    w = input()
    if w in A.keys():
        print(*A[w], " ")
    else:
        print("-1")
