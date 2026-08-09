
import math
while True:
    print("1. Celsius to Fahrenheit Conversion")
    print("2. Fahrenheit to Celsius Conversion")
    print("3. Calculate Area of Circle")
    print("4. Calculate Area of Rectangle")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"Temperature in Fahrenheit: {fahrenheit:.2f} °F")

    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"Temperature in Celsius: {celsius:.2f} °C")

    elif choice == 3:
        radius = float(input("Enter radius of the circle: "))
        area = math.pi * radius ** 2
        print(f"Area of Circle: {area:.2f} square units")

    elif choice == 4:
        length = float(input("Enter length of the rectangle: "))
        width = float(input("Enter width of the rectangle: "))
        area = length * width
        print(f"Area of Rectangle: {area:.2f} square units")

    elif choice == 5:
        print("Thank you")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")




