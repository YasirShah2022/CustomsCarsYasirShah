# Display a title block for the program opening
print("***************************")
print("Welcome to the UMBC")
print("Car Customiztion Form!")
print("***************************")
print()
print()

# Decide on the the six options for the car
print("(For multiple choice questions, please enter the letter of the selection you're looking for)")
print()
print("          ~ Make & Model ~")
# Create input propmts for the user to select the options and store them in variables
print("1. What Model of Car are you ordering?")
print("  a. Lightining Speedster")
print("  b. Eco Leaf")
print("  c. Harp Chord")
print("  d. Chvron Jolt")
# Assign variables for the six options
modelOption = input("Please enter 'a' - 'd': ")
print()
# Prompt question 2
print("2. Would you like to upgrade from the 4-door option to the 2-door option?")
# Question 2 variable assignment 
bodyStyle = input("Please enter 'yes' or 'no': ")
print()
print()
print("          ~ Exterior~")
# Prompt question 3
print("3. What color would you like your car to be?")
# Question 3 variable assignment 
color = input("You may enter the name of any color you'd like: ")
print()
# Prompt question 4
print("4. Would you like the deluxe weather package?")
# Question 4 variable assignment 
pkg = input("Please enter 'yes' or 'no': ")
print()
print()
print("          ~ Interior ~")
# Prompt question 5
print("5. Which Engine would you like your car to have?")
print("  a. I-4 Entry Engine")
print("  b. V-6 Performance Engine")
print("  c. Eco Diesel Engine")
print("  d. Electric Motor Drive")
# Question 5 variable assignment
engine = input("Please enter 'a' - 'c': ")
print()
# Prompt question 6
print("6. Would you like heated seats?")
# Question 6 variable assignment 
seatHeat = input("Please enter 'yes' or 'no': ")
print()
print()
# Print a summary of the car options for the dealership
# based on the selected options and variable arguments
print("==================================================")
print(" ~ Summary ~ ")
print(f'Model Option: {modelOption}')
print(f'Upgrade to 2-Door: {bodyStyle}')
print(f'Desired Color: {color}')
print(f'Upgrade to Deluxe Weather: {pkg}')
print(f'Engine Option: {engine}')
print(f'Upgrade to Heated Seats: {seatHeat}')