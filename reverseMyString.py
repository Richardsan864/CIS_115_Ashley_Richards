# Get user input and assign it to a variable.
input_string = input("Enter a word: ")

# Define a function that reverses the string inputed.

def reverseMyString():
    reversedString = input_string[::-1]
    print(reversedString)

# Call the function and print the reversed string
reverseMyString()