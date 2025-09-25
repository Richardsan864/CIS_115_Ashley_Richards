# Get input from user for number of loops to perform.
Num_loops = int(input("Enter the number of loops you want to perform: "))
print("You want to perform ", Num_loops, " loops.")

# Use for-in loop to loop the requested number of times.

for counter in range(Num_loops):
    print("This is loop number: ", counter + 1)

print("The user has performed ", Num_loops, " loops.")

