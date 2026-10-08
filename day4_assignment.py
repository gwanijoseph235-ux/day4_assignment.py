# COLLECTING USER SCORES
print("=== STUDENT GRADING SYSTEM ===")
print()

name = input("Enter your name: ")
score = int(input("Enter your score: "))

# Determining the letter grade based boundary conditions

if score >= 70 and score <= 100:
    grade = "A"
elif score >= 60 and score < 70:
    grade = "B"
elif score >= 50 and score < 60:
    grade = "C"
elif score >= 45 and score < 50:
    grade = "D"
elif score >= 0 and score < 45:
    grade = "F"
else:
    grade = "Invalid (must be between 0 and 100)"

# Displaying Grade output
print(f"Your score is {score}.")
print(f"Your grade is {grade}.")
