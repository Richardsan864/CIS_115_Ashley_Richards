# Program to determine if a number < or > and valid or invalid

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 - num2
print(("The answer is: "), result)
if result < 0:
    print("#################################\nInvalid! The value is less than zero.\n#################################")

else:
    print("The values entered were valid integers.")