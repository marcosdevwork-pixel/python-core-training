#==============================================
# EXERCISE 1 - BASIC STRING ASSIGNMENT
#==============================================

# Store a text message inside a variable
message = "Hello, Python!"

# Print the message to the screen
print(message)

#==============================================
# EXERCISE 2 - RAW STRING CONCATENATION
#==============================================

# Ask the user for two texts
text_1 = input("Enter a text: ")
text_2 = input("Enter one more: ")

# Join texts exactly as they were typed (no space)
result = text_1 + text_2

# Print the combined message
print(f"Result: {result}")

#==============================================
# EXERCISE 3 - PHRASE CONCATENATION
#==============================================

# Ask the user for two words or small test
first_part = input("Enter a text: ")
second_part = input("Enter one more: ")

print(f"Result: {first_part} {second_part}")

#==============================================
# EXERCISE 4 - STRING LENGTH
#==============================================

# Ask the user for a text
text = input("Enter a text: ")

# Count the number of characters in the text
amount = len(text)

# Print the result
print(f"The text has {amount} characters.")

#==============================================
# EXERCISE 5 - STRING CASE & CLEANING
#==============================================

# Ask the user to enter a phrase with capital letters and extra spaces
text = input("Enter a phrase with capital letters and extra spaces: ")

# Store the original text for reference
original = text

# Remove extra spaces at the beginning and end of the text
without_extra_spaces = original.strip()

# Convert the text to lowercase to normalize it
normalized = without_extra_spaces.lower()

# Print the original text
print(f"Original: {original}")

# Print the text without extra spaces
print(f"Without extra spaces: {without_extra_spaces}")

# Print the normalized text (all lowercase)
print(f"Normalized: {normalized}")

#==============================================
# EXERCISE 6 - STRING REPLACEMENT
#==============================================

# Ask the user for a phrase or a file name
text = input("Enter a phrase or file/folder name: ")

# Replace spaces with underscores to prepare for file names/folders
edit = text.replace(" ","_")

# Print the original text
print(f"Original: {text}")

# Print the edited text
print(f"With replace: {edit}")

#==============================================
# EXERCISE 7 - STRING CHECKING
#==============================================

# Ask the user to enter a file
file_name = input("Enter a file name: ")

# Print the original file name
print(f"Original: {file_name}")

# Convert the file name to lowercase for safe checking
edited = file_name.lower()

# Print the normalized file
print(f"Edited file name: {edited}")

# Check if the file has a .txt extension
if edited.endswith(".txt"):
    print(f"{edited} is a text file.")

# Check if the file starts with "report_"
elif edited.startswith("report_"):
    print(f"{edited} is a report file.")

# Check if the file name starts with "img_"
elif edited.startswith("img_"):
    print(f"{edited} is an image file.")

# If none of the conditions match
else:
    print(f"{file_name} is not a text file.")

#==============================================
# EXERCISE 8 - STRING SPLIT
#==============================================

# Ask the user to enter a file name
file_name = input("Enter file name to process: ")

# Show the original file name
print(f"Original file name: {file_name}")

# Create variables to check the file name structure
has_dot = "." in file_name
has_underscore = "_" in file_name

# Check if file has an extension
if has_dot:
    parts = file_name.split(".")
    name = parts[0]
    extension = parts[1]
    print(f"Name without extension: {name}")
    print(f"Extension name: {extension}")

    # If has extension, check for underscore in the name
    if has_underscore:
        name_parts = name.split("_")
        print(f"Name parts: {name_parts}")
# If the file has no extension, check for underscore
elif has_underscore:
    name_parts = file_name.split("_")
    print(f"Name parts: {name_parts}")

# If file has no extension and no underscore, inform the user
else:
    print(f"{file_name} has no extension and no underscore.")

#==============================================
# EXERCISE 9 - STRING MEMBERSHIP (in / not in)
#==============================================

# Ask the user for a file name
file_name = input("Enter a file name: ")

# Print the original file name
print(f"Original file name: {file_name}")

# Normalize the file name (remove spaces and convert to lowercase)
normalized_name = file_name.strip().lower()

# Check if the file contains the word "backup"
if "backup" in normalized_name:
    print("This file contains the word backup")
else:
    print("This file does not contain the word backup")

# Check if the file does not contain the word "temp"
if "temp" not in normalized_name:
    print("This file does not contain the word temp")
else:
    print("This file contains the word temp")

#==============================================
# EXERCISE 10 - BASIC STRING VALIDATION
#==============================================

# Ask the user for a file
file_name = input("Enter a file name: ")

# Print the original file name
print(f"Original file name: {file_name}")

# Normalize the file name(remove spaces and convert to lowercase)
normalized_name = file_name.strip().lower()

# Check if the normalized file name is empty
if len(normalized_name) == 0:
    print("Invalid file. You entered only spaces or nothing.")
else:
    print("Valid file.")