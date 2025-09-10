#Ask user for imput
Num1 = float(input("Enter first number: "))
Num2 = float(input("Enter second number: "))
Num3 = float(input("Enter third number: "))
Add = (Num1) + (Num2)
divide = (Add) / float(Num3)
print("The answer is: ", divide)

#Print if else statement to see if number is (>) or (<) 0.

if divide > 0:
    print("The mathematical operation is > than 0.")
else:
    print(f"The mathematical operation is <= 0.")