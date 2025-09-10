# Program to determine if a number < or > and valid or invalid

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 - num2

if result < 0:
    print("Invalid! The value is less than zero.")
else:
    print("The values entered were valid integers.")