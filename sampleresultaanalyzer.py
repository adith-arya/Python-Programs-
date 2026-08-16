names = ["Arun", "Bala", "Charan", "Divya", "Esha"]
marks = [85, 72, 38, 105, 91]

valid = 0

for i, (name, mark) in enumerate(zip(names, marks), start=1):
    if mark < 0 or mark > 100:
        print("Invalid marks for", name, "- Skipped")
        continue

    if mark >= 80:
        grade = "Excellent"
    elif mark >= 60:
        grade = "Good"
    elif mark >= 40:
        grade = "Average"
    else:
        grade = "Fail"

    print(i, ".", name, "-", mark, "-", grade)
    valid += 1

print("\nTotal Valid Students:", valid)
