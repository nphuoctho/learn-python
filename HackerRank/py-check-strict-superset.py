A = set(map(int, input().split()))
n = int(input())

if all(A.issuperset(set(map(int, input().split()))) for _ in range(n)):
    print(True)
else:
    print(False)
