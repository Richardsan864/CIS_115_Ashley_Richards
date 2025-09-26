import math

# Get user input for 2 sides of the triangle.
# Assign the numbers to a variable

side_x = float(input("Enter the length of side A: "))
side_y = float(input("Enter the length of side B: "))

# Enter the formula for the Pathagorean Theorem and assign it to a variable.

theorum = float(math.sqrt(side_x**2 + side_y**2))

print("The hypoteneuse is: ", theorum)