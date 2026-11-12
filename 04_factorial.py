# Program 4: Find the factorial of a non-negative integer

number = int(input("Enter a non-negative whole number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1

    # Multiply all integers from 1 up to the entered number
    for i in range(1, number + 1):
        factorial = factorial * i

    print("Factorial of", number, "is", factorial)
