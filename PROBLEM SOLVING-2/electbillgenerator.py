n = int(input("Enter number of consumers: "))

for i in range(n):
    name = input("Consumer " + str(i + 1) + ": ")
    units = int(input("Units: "))

    if units < 0:
        print("Invalid units for", name, "- Skipped")
        continue

    if units == 0:
        print("0 units entered. Processing stopped.")
        break

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = units * 3
    elif units <= 300:
        bill = units * 5
    else:
        bill = units * 7

    print(name, "-", units, "units - Bill: ₹" + str(bill))
