# Write a function where mass = 3kg and c = 2.99 x 10**8.

def energy_problem():
    mass = float(3)
    acceleration = float(2.99 * 10**8)
    energy = mass * acceleration
    print("The energy produced using 3kg of mass is", float(energy), "Joules")

energy_problem()

# Write a def function to set up the calculation problem.
# Make sure the numbers are a floating point value.
# Ask for user input for mass in kg.

def calculate_energy():
    mass = float(input("Enter the mass in kg: "))
    c = float(2.99 * 10**8)
    acceleration = mass * c
    print("The energy produced is: ", acceleration, "Joules")
calculate_energy()
