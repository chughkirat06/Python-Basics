#  Grade calculator

""""
Assign a letter grade based on a student's score:
A (90-100),
B (80-89),
C (70-79),
D (60-69),
F (below 60).
"""

#  Get student's score
score = int(input("Enter student's score (0-100): "))

if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
elif 0 <= score < 60:
    print("F")
else:
    print("Invalid score")