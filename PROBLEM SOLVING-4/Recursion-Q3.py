def digit_sum(number):

    if number < 10:
        return number

    digit = number % 10

    return digit + digit_sum(number // 10)


number = 5824

print("Sum of digits:", digit_sum(number))
