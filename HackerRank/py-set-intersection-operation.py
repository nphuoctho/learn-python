# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eng_subs = set(map(int, input().split()))

b = int(input())
french_subs = set(map(int, input().split()))

print(len(eng_subs.intersection(french_subs)))
