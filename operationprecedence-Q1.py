def evaluate(m1, m2, m3, attendance):
    average = (m1 + m2 + m3) / 3
    if (m1 >= 40 and m2 >= 40 and m3 >= 40):
        if average >= 75 and attendance >= 75:
            return average, "Eligible"
    return average, "Not Eligible"

data = input("Enter marks and attendance: ").split()
m1 = float(data[0])
m2 = float(data[1])
m3 = float(data[2])
attendance = float(data[3])
result = evaluate(m1, m2, m3, attendance)
print("Average:", result[0])
print("Status:", result[1]) 
