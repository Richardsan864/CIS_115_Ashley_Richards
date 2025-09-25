#Get user input for a number between 1 and 100.
num = int(input("Enter a number between 1 and 100: "))

# use while loop to keep asking for a number
# until they enter an invalid number.

while num >= 1 and num <= 100:
# Check if number is in range.
    print("Valid number.")
    num = int(input("Enter a number between 1 and 100. "))
# Check if number is in range.
print("Sorry, the number you entered is out of range.")
   

