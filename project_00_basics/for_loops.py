#==============================================
# EXERCISE 1 - BASIC FOR LOOP
#==============================================

# Repeat this loop five times
for i in range(5):

    # Print the loop message
    print("This is the first exercise.")

#==============================================
# EXERCISE 2 - COUNTING WITH FOR LOOP
#==============================================

# Ask the user for a number
number = int(input("Enter a number: "))

# Loop from 1 up to the selected number
for n in range(1, number + 1):
    # Print each value
    print(n)

#==============================================
# EXERCISE 3 - COUNTING BACKWARDS
#==============================================

# Ask the user for another number
number = int(input("Enter another number: "))

# Loop for the number down to 1
for i in range(number, 0, -1):

    # Print each value
    print(i)