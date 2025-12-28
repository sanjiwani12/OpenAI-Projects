print("Student Grade Calculator")

subject_count = int(input("Enter the number of subjects: "))

while subject_count <= 0:
    print("Invalid number of subjects. Please enter a positive number.")
    subject_count = int(input("Enter the number of subjects: "))

print(f"You have {subject_count} subjects.")

total_score = 0

print(f"Total so far: {total_score}")

for i in range(subject_count):
    score = int(input(f"Enter score for subject {i+1}: "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter a value between 0 and 100.")
        score = int(input(f"Enter score for subject {i+1}: "))

    total_score += score


average_score = total_score / subject_count

print(f"Your average score is: {average_score:.2f}")

if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

print("--- Student Report ---")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score:.2f}")
print(f"Grade: {grade}")


