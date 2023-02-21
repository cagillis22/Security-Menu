'''Menu-Driven Python Application'''
# Courtney Gillis
# 1/31/23
# Lab 2
# A command line menu-driven python application providing users with the
# ability to perform several math and security related functions.


def menu():
    '''Function calling the menu selection process'''
    # Menu options for the user to choose from
    print("Welcome to the Main Menu!\n")
    print("Select an option from the list below:")
    print("a. Generate a Secure Password")
    print("b. Calculate and Format a Percentage")
    print("c. How many days from today until July 4,2025?")
    print("d. Use the Law of Cosines to calculate the leg of a triangle")
    print("e. Calculate the volume of a Right Circular Cylinder")
    print("f. Exit the program")
    print("\n")
# Calls the menu selection process
menu()
# Asks the user choose a menu option
choice = input("Please select a menu option: ")
# Option a: Prompts the user for the length of their desired password
if choice == "a":
    import secrets
    import string
    # Asks the user for the password length
    length = int(input("Please enter the length of your password: "))
    # Checks that the password length is between 6 and 30
    while length < 6 or length > 30:
        print("Your password length must be between 6 and 30 characters")
        length = int(input("Please enter the length of your password: "))
    # Generates a password with randomized uppercase letters, lowercase letters, numbers, and special characters
    PASSWORD = "".join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
    # Prints the generated password for he user
    print("Your generated secure password is: " + PASSWORD)
# Option b: Prompts the user to enter a numerator and a denominator to calculate their percentage
elif choice == "b":
    # Asks the user to input a numerator and a denominator
    number_1 = float(input("Please enter your first number: "))
    number_2 = float(input("Please enter the second number: "))
    # Calculates the precentage of the numbers
    percentage = round((number_1/number_2)*100, 2)
    # Prints the calculated percentage or the user
    print("The percentage is: " + str(percentage) + "%")
# Option c: Calculates the remaining Days Until July 4, 2025
elif choice == "c":
    import datetime
    # Determines the current date
    today = datetime.date.today()
    # Calculates the difference between the current date and 7/4/2025
    date = datetime.date(2025, 7, 4)
    difference = date - today
    # Calculates the remaining days until 7/4/2025
    remaining_days = difference.days
    # Prints the remaining days until 7/4/2025 for the user
    print("There are " + str(remaining_days) + " remaining days until July 4, 2025")
# Option d: Uses the Law of Cosines to calculate the leg of a  for the user
elif choice == "d":
    import math
    # Asks the user to input side A, side B, and Angle C of their triangle
    a = float(input("Please enter the length of side A: "))
    b = float(input("Please enter the length of side B: "))
    c = float(input("Please enter the angle C between sides A and B: "))
    # Calculates side C of the triangle using the Law of Cosines
    c = round(math.sqrt(a**2 + b**2 - (2 * a * b * math.cos(math.radians(c)))), 2)
    # Print Side C
    print("The length of the leg of your triangle is: " + str(c))
# Option e: Calculates the Volume of a Right Circular Cylinder
elif choice == "e":
    import math
    # Asks the user for the radius and height of their cylinder
    radius = float(input("Please enter the radius of the cylinder: "))
    height = float(input("Please enter the height of the cylinder: "))
    # Calculates the volume from the users numbers
    volume = round(math.pi * (radius ** 2) * height, 2)
    # Prints the volume of the cylinder
    print("The volume of your cylinder is: " + str(volume))
# Exits the program
elif choice == "f":
    import sys
    sys.exit("Thank you for using the Main Menu!")
# Registers an invalid input and asks the user to re-enter their response
else:
    print("Please enter a valid menu option.")
    menu()
    