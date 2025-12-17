#==============================================
#        EXERCISE OF MATH OPERATIONS
#==============================================

# Ask the user for two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Perform all math operations
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2
integer_division = number1 // number2
modulus = number1 % number2
power = number1 ** number2
absolute_difference = abs(number1 - number2)

# Print all results
print("\nResults:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Integer division: {integer_division}")
print(f"Modulus: {modulus}")
print(f"Power: {power}")
print(f"Absolute difference: {absolute_difference}")
