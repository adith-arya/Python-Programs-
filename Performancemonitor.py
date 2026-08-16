names = ["Anu", "Bharath", "Chitra", "Deepak", "Farah"]
attendance = [92, 68, 85, 45, 78]
marks = [88, 55, 76, 32, 91]

eligible = 0

for i, (name, attend, mark) in enumerate(zip(names, attendance, marks), start=1):

    if attend < 0 or attend > 100 or mark < 0 or mark > 100:
        continue

    if attend >= 75:
        eligible += 1

        if mark >= 80:
            result = "Distinction"
        elif mark >= 60:
            result = "First Class"
        elif mark >= 40:
            result = "Pass"
        else:
            result = "Fail"

        print(i, "-", name, "- Attendance:", str(attend) + "% - Marks:", mark, "-", result)

    else:
        print(i, "-", name, "- Attendance:", str(attend) + "% - Not Eligible")

print("Total Eligible Students:", eligible)
