# Make a user defined function named print_message1.
# Under this function print the first statement.

def print_message1():
    print("I was called first")
    print_message2()

# Define antoher function named print_message2.
# In this function print statement 2.
def print_message2():
    print("I was called from print_message1")

# Print message by calling function 1.
print_message1()