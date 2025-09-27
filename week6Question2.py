# Define your 2 functions names.

def print_message1():
    print("I was called first")
    print_message2()

def print_message2():
    print("I was called from print_message1")

# Print message by calling function 1.
print_message1()