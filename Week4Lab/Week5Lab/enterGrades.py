# define counter.
counter = 0

# Get input for number of grades being entered
Num_grades = int(input("Enter the number of grades you want to input: "))
print("You want to input ", Num_grades, " grades.")

# Use while loop to get grades.
#Print the number entered.
while counter < Num_grades:
    grade = input("Enter a grade: ")
    print("You entered: " + grade)
    counter = counter + 1

print("The user has entered", Num_grades, "grades.")