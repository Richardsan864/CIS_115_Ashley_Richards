# Get users credit card number
ccNum = input("Please enter your credit card number: ")

def validCreditCard(ccNum):
    # Reverse the card number
    ccNum = (ccNum[::-1])
    
    # Get every other number (even)
    even_nums = ccNum[::2]

    # Change each even number to an int
    even = []
    for num in even_nums:
        even.append(int(num))

    # Sum all of the even numbers
    total_even = sum(even)

    # Get every other number (odd)
    odd_nums = ccNum[1::2]

    # Change every odd number to an int
    odd = []
    for num in odd_nums:
        odd.append(int(num))
    # Establish the counter at zero
    total_odd = 0
    # Multiply the "odd" numbers by 2
    for value in odd:
        new_odd = value * 2
        # Use if/else to minus 9 if number is greater than 9
        if new_odd > 9:
            total_odd += (new_odd - 9)
        else:
            total_odd += new_odd
    # sum both sets of numbers
    total = total_even + total_odd
    # Set up True/False values
    if total % 10 == 0:
        return True
    else:
        return False
# Use while loop to validate the ccNum 
# use if/else to address the users input and either approve of invalidate the card number
while True:
    if validCreditCard(ccNum):
        print(f'The credit card number', ccNum, 'is valid!') 
        break
    else:
        print(f'Invaild credit card entered. Please try again.' )
        ccNum = input("Please enter your credit card number: ")   
     
# Assign the validateCreditCard(ccNum) to result while calling the def function and print result
result = validCreditCard(ccNum)
print(result)
