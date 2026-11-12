# Program 2: Check whether a number is even or odd

number = int(input("Enter a whole number: "))

# A number is even when its remainder after division by 2 is 0
if number % 2 == 0:
    print(number, "is an even number")
else:
    print(number, "is an odd number")
