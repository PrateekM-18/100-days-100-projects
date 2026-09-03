import math


# FUNCTIONS

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def square(a):
    return a ** 2


def sq(a):
    if a < 0:
        return "Cannot find square root of negative number"
    return math.sqrt(a)


def power(a, b):
    return math.pow(a, b)


# INPUTS

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


# CHOICES

print("--------------------------------------------")
print("Operations and Choices")
print("1 : Addition")
print("2 : Subtraction")
print("3 : Multiplication")
print("4 : Division")
print("5 : Square")
print("6 : Square Root")
print("7 : Power")
print("--------------------------------------------")


# OPERATION CHOICE

choice = input("Enter the choice of operation: ")

print("--------------------------------------------")


# OUTPUT

if choice == '1':
    print(f"Addition of {num1} and {num2} is: {add(num1, num2)}")

elif choice == '2':
    print(f"Subtraction of {num2} from {num1} is: {sub(num1, num2)}")

elif choice == '3':
    print(f"Multiplication of {num1} and {num2} is: {multiply(num1, num2)}")

elif choice == '4':
    print(f"Division of {num1} by {num2} is: {divide(num1, num2)}")

elif choice == '5':
    print(f"Square of {num1} is: {square(num1)}")

elif choice == '6':
    print(f"Square Root of {num1} is: {sq(num1)}")

elif choice == '7':
    print(f"Power of {num1} to {num2} is: {power(num1, num2)}")

else:
    print("Invalid choice")