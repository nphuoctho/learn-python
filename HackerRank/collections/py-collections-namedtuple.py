from collections import namedtuple

N = int(input())

Students = namedtuple("Students", input().split())

total_marks = 0
for _ in range(N):
    student = Students(*input().split())
    total_marks += int(student.MARKS)

print(f"{total_marks / N:.2f}")
