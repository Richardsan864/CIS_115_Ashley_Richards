# Import the math function
import math

#Have user input sides X and Y.
# Assign these to a variable with a floating point number.
x = float(input("Please enter the number in degrees for side x: "))
y = float(input("Please enter the number in degrees for side y: "))

# Use math.atan2(y,x) to set up your calculations.
# Clculate side C and label in degrees.
angle_radians = math.atan2(y,x)
side_c = angle_radians * (180 / math.pi)

print("The answer is", side_c, "degrees")