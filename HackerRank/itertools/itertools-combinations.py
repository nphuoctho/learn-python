# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s, k = input().split()
s = sorted(list(s.upper()))
k = int(k)

arr = []
for i in range(1, k + 1):
    arr.extend(sorted(list(combinations(s, i))))

[print("".join(e)) for e in arr]
