from itertools import permutations

S = input().split()


list_permutatios = list(permutations("".join(sorted(S[0])), int(S[1])))


[print("".join(e)) for e in list_permutatios]
