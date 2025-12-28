#==============================================
# EXERCISE 1 - BASIC DICTIONARY CREATION
#==============================================

# Create an empty dictionary to store file information
file_info = {}

# Add file name to dictionary
file_info["name"] = "report_2025"

# Add file extension to dictionary
file_info["extension"] = ".pdf"

# Add file size to dictionary
file_info["size"] = "2048"

# Access values from the dictionary and store in variables
name = file_info["name"]
extension = file_info["extension"]
size = file_info["size"]

# Print the file information
print(f"File name: {name}")
print(f"Extension: {extension}")
print(f"Size: {size}")
print("--------------------")

#==============================================
# EXERCISE 2 - UPDATING DICTIONARY VALUES
#==============================================

# Create a dictionary with initial file information
file_info = {
    "name": "report_2025",
    "extension": ".pdf",
    "size": "2048"
}

# Update the file size
file_info["size"] = "2450"

# Access values in the dictionary and store in variables
name = file_info["name"]
extension = file_info["extension"]
size = file_info["size"]

# Print the updated file information
print(f"Name: {name}")
print(f"Extension: {extension}")
print(f"Size: {size}")
print("--------------------")

#==============================================
# EXERCISE 3 - ADDING NEW DICTIONARY KEYS
#==============================================

# Create a dictionary with initial file information

file_info = {
    "name": "report_2025",
    "extension": ".pdf",
    "size": "2450"
}

# Add create date and author to the dictionary
file_info["created_date"] = "12/27/2025"
file_info["author"] = "Marcos"

# Access the values from dictionary and store in variables
name = file_info["name"]
extension = file_info["extension"]
size = file_info["size"]
created_date = file_info["created_date"]
author = file_info["author"]

# Print all file information
print(f"Name: {name}")
print(f"Extension: {extension}")
print(f"Size: {size}")
print(f"Created date: {created_date}")
print(f"Author: {author}")
print("--------------------")

#==============================================
# EXERCISE 4 - CHECKING DICTIONARY KEYS
#==============================================

# Create a dictionary with file information
file_info = {
    "name": "report_2025",
    "extension": ".pdf",
    "size": "2450"
}

# Check if the "author" key exists before accessing it
if "author" in file_info:
    print(f"Author: {file_info['author']}")
else:
    print("Author key does not exist")
print("--------------------")

#==============================================
# EXERCISE 5 - LOOPING THROUGH DICTIONARIES
#==============================================

# Create a dictionary with file information
file_info = {
    "name": "report_2025",
    "extension": ".pdf",
    "size": "2450",
    "created_date": "12/28/2025",
    "author": "Marcos"
}

# Loop throungh the dictionary with file information
for key, value in file_info.items():
    print(f"{key}; {value}")
print("--------------------")

#==============================================
# EXERCISE 6 - REAL AUTOMATION SCENARIO (MINI)
# Counting files by extension
#==============================================

# Dictionary to store extension counts
extension_report = {}

# Simulated list of files
files = [
    "report_2025.pdf",
    "notes.txt",
    "image.jpg",
    "report_backup.pdf",
    "data.txt"
]

# Loop through each file name
for file_name in files:
    
    # Print the current file name
    print(file_name)

    # Extract the file extension from the file name
    extension = file_name.split(".")[1]

    # If the extension already exists, increment its counts
    if extension in extension_report:
        extension_report[extension] = extension_report[extension] + 1
    
    # If the extension does not exist, initialize it with 1
    else:
        extension_report[extension] = 1
    
    # Print the result
    print(extension_report)