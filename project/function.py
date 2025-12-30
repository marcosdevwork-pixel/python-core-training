#==============================================
# EXERCISE 1 - BASIC FUNCTION CREATION
#==============================================

def say_hello():
    print("Hello")

say_hello()

#==============================================
# EXERCISE 2 - FUNCTIONS WITH PARAMETERS
#==============================================

def greet_person(name):

    # Print a greeting using the provided name
    print(f"Hello {name}")

# Call the function with different names
greet_person("Marcos")
greet_person("Filipe")

#==============================================
# EXERCISE 3 - FUNCTIONS WITH RETURN VALUES
#==============================================

# Define a function that calculates the square of a number
def square_number(num):

    # Calculate the square of the number
    return num ** 2

# Call the function with an argument and store the result
result = square_number(4)

# Print the returned value
print(result)

#==============================================
# EXERCISE 4 - FUNCTIONS WITH DEFAULT PARAMETERS
#==============================================

# Define a function with a default parameter
def greet(name="guest"):

    # Print a greeting using the provided name or the default
    print(f"Hello {name}")

# Call the function without argument (uses default)
greet()

# Call the function with an argument (overrides default)
greet("Marcos")

#==============================================
# EXERCISE 5 - PRACTICAL FUNCTIONS FOR AUTOMATIONS
#==============================================

def create_file_name(name, number=1):

    # Building a file name using the base name and the number
    file_name = f"{name}_{number}.txt"

    # Return the generated file name
    return file_name 

# Call the function without passing the number (default value is used)
file_name = create_file_name("text1")

# Print the returned file name
print(file_name)