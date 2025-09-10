#Modulo operator to find even or odd numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 % num2

if result % 2 == 0:
    print("The number is an even number.")
else:
    print("The number is odd.")