#================================================
# EXERCISE 1 - SIMPLE WHILE LOOP
#================================================

# Initiallize counter
counter = 0

# Repeat while counter is less than five
while counter < 5:

    # Print the loop message
    print("This is the first while loop.")

    # Increase counter by 1
    counter +=1

#================================================
# EXERCISE 2 - USER INPUT LOOP
#================================================

#  Tells how to stop the loop
print("0 is the number to stop the loop.")

# Ask the user for a number
number = int(input("Enter a number: "))

# Repeat the loop while the number is not zero
while number != 0:

    # Inform the user that the loop continues
    print("The loop continues")

    # Ask for a new number
    number = int(input("Enter a number: "))

#================================================
# EXERCISE 3 - CONDITIONAL LOOP WITH IF/ELIF/ELSE
#================================================

# Inform the user how to stops the loop
print("Zero is the number to stop the loop.")

# Starts an infinite loop
while True:

    # Ask the user for a number
    number = int(input("Enter a number: "))

    # Check if the number is positive
    if number > 0:
        print(f"{number} is a positive number.")

    # Check if the number is negative
    elif number < 0:
        print(f"{number} is a negative number.")

    # The number is zero, stop the loop
    else:
        print("End")
        break