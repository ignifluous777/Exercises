print("Enter a value between 0-100 for student grade: ")
mark = int(input())

if mark >= 90 and mark <= 100:
    grade = "A+ GRADE"
if mark >= 70 and mark <= 89:
    grade = "B GRADE"
if mark >= 50 and mark <= 69:
    grade = "C GRADE"
if mark >= 35 and mark <= 49:
    grade = "D GRADE"
if mark < 35:
    grade = "FAIL"

print(grade)
