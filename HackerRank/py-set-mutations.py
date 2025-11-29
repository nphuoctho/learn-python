n = int(input())
A = set(map(int, input().split()))

N = int(input())
for _ in range(N):
    cmd, len = input().split()
    B = set(map(int, input().split()))

    if cmd == "update":
        A.update(B)
    elif cmd == "intersection_update":
        A.intersection_update(B)
    elif cmd == "difference_update":
        A.difference_update(B)
    elif cmd == "symmetric_difference_update":
        A.symmetric_difference_update(B)
        
print(sum(A))
