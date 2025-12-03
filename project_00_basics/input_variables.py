#==================================
# FIRST EXERCISE --> NAME AND AGE
#===================================
print("=== User Information ===")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
# Input: Ask the user for their name and age 

print(f"Hello {name}, you are {age} years old.")
# Output: Prints a greeting using the information provided

#==================================
# SECOND EXERCISE --> BIRTH YEAR
#==================================
print("\n=== Birth Year ===")

current_year = 2025
# Define current year

birth_year = current_year - age
# Calculate birth year using the previously entered age

print(f"You were born in {birth_year}.")
# Prints birth year

#==================================
#THIRD EXERCISE --> AGE IN 10 YEARS
#==================================

print("\n=== Age in 10 Years ===")

age_in_10_years = age + 10
# Calculate user's age in 10 years 

print(f"In 10 years you will be {age_in_10_years}.")
# Prints the result
