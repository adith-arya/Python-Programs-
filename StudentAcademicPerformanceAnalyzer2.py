# Student Academic Performance Analyzer
student_name = input("Enter student name: ")
usn = input("Enter USN: ")

mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))
mark4 = float(input("Enter marks for Subject 4: "))
mark5 = float(input("Enter marks for Subject 5: "))

total_marks = mark1 + mark2 + mark3 + mark4 + mark5
percentage = (total_marks / 500) * 100
average = total_marks / 5

if percentage >= 90:
    grade = "O"
elif percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "RA"

print(f"Student Name : {student_name}")
print(f"USN          : {usn}")

print("\nMarks:")
print(f"Subject 1    : {mark1:.2f}")
print(f"Subject 2    : {mark2:.2f}")
print(f"Subject 3    : {mark3:.2f}")
print(f"Subject 4    : {mark4:.2f}")
print(f"Subject 5    : {mark5:.2f}")

print(f"Total Marks  : {total_marks:.2f} / 500")
print(f"Percentage   : {percentage:.2f}%")
print(f"Average      : {average:.2f}")
print(f"Grade        : {grade}")
