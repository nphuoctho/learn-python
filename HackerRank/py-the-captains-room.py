K = int(input())
A = list(map(int, input().split()))

unique_rooms = set(A)
total_unique = sum(unique_rooms)
total_all = sum(A)
captains_room = (total_unique * K - total_all) // (K - 1)
print(captains_room)
