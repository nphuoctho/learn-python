from collections import Counter

X = int(input())
sizes = Counter(list(map(int, input().split())))
N = int(input())

total = 0
for _ in range(N):
    size, price = list(map(int, input().split()))
    if sizes[size]:
        sizes[size] -= 1
        total += price

print(total)
