#==============================
#     CONDITIONS IF/ELSE
#==============================

# Ask the user for a number
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

#==============================
#   CONDITIONS IF/ELIF/ELSE
#==============================

# Ask the user for another number
number = int(input("Enter another number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print("The number is zero.")

#==============================
#   CHECK FILE EXTENSION .TXT
#==============================

# Ask the user for a file name
file_name = input("Enter a file name: ").strip()

# Check if the file ends with '.txt'
if file_name.lower().endswith(".txt"):
    print(f"{file_name} is a text file")
else:
    print(f"{file_name} is not a text file.")

#==============================
#   CHECK FILE PREFIX
#==============================

# Ask the user for another file name
file_name = input("Enter another file name: ").strip()

# Check if the file starts with 'report_'
if file_name.lower().startswith("report_"):
    print(f"{file_name} is a report file.")

# Check if the file starts with 'img_'
elif file_name.lower().startswith("img_"):
    print(f"{file_name} is an image file.")

# Handle cases where the prefix is not recognized
else:
    print(f"{file_name} has no recognized prefix.")