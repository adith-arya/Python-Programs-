marks = [35, 60, 45, 80, 35, 55, 60, 95, 40, 80]

# Remove marks below 40
filtered_marks = [mark for mark in marks if mark >= 40]

# Remove duplicates and sort in ascending order
unique_marks = sorted(set(filtered_marks))

# Identify marks greater than or equal to 60
qualified = [mark for mark in unique_marks if mark >= 60]

# Display the three highest qualifying marks
top_three = sorted(qualified, reverse=True)[:3]

print("Processed marks:", unique_marks)
print("Qualified marks:", qualified)
print("Top three:", top_three)
