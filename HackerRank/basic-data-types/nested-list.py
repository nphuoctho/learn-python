"""
Nested Lists

Difficulty Level: Easy
"""

if __name__ == "__main__":
    student_marks = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_marks.append([name, score])

    unique_scores = sorted(list(set([score for name, score in student_marks])))
    second_lowest_score = unique_scores[1] if len(unique_scores) > 1 else None

    second_lowest_students = []
    if second_lowest_score is not None:
        for name, score in student_marks:
            if score == second_lowest_score:
                second_lowest_students.append(name)

        second_lowest_students.sort()

        for student in second_lowest_students:
            print(student)
