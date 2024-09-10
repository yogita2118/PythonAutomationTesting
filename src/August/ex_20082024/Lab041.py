# Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score ( e.g., A, B, C, D, or F)
# based on the following grading scale:
#
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# E: 35-59
# F: 0-34

# Logic Building Formula

# 1 -> User Inputs -> score or marks -> int
# 2 -> o/p -> str -> A or B...


score = int(input("Enter your score\n"))

if 90 <= score <= 100:
    grade = "A"
    print("Your grade ", "A")
elif 80 <= score <= 89:
    grade = "B"
    print("Your grade ", "B")
elif 70 <= score <= 79:
    grade = "C"
    print("Your grade ", "C")
elif 60 <= score <= 69:
    grade = "D"
    print("Your grade ", "D")
elif 35 <= score <= 59:
    grade = "E"
    print("Your grade ", "E")
elif score >= 100:
    print("You are Supermen! !")
else:
    grade = "F"
    print("Your grade is ", "F")
