#==============================================
# EXERCISE 1 - CHECK IF A FILE EXISTS
#==============================================

import os 

# Define the file name to check
file_name = "example.txt"

# Check if the file exists in the current working directory
if os.path.exists(file_name):
    print("The file exists")
else:
    print("The file does not exist")


#==============================================
# EXERCISE 2 - CREATE A FILE
#==============================================

# Define the file name to be created
file_name = "example.txt"

# Create the file only if it does not exist
if not os.path.exists(file_name):
    with open(file_name, "w") as file:
        # Write initial content to the file
        file.write("This file was created by Python.")
    print("File created successfully")
else:
    print("File already exists")


#==============================================
# EXERCISE 3 - CREATE A FOLDER
#==============================================

# Define the folder name to be created
folder_name = "example_folder"

# Create the folder only if it does not exist
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created successfully")
else:
    print("Folder already exists")


#==============================================
# EXERCISE 4 - LIST FILES IN A DIRECTORY
#==============================================

# Define the directory to list files from
directory = "."

# List all files and folders inside the directory
items = os.listdir(directory)

# Print each item found in the directory
for item in items:
    print(item)


#==============================================
# EXERCISE 5 - PRACTICAL AUTOMATION
#==============================================

# Define source and destination folders
source_folder = "."
destination_folder = "example_folder"

# Ensure destination folder exists
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

# Move all .txt files to the destination folder
for item in os.listdir(source_folder):
    if item.endswith(".txt"):
        source_path = os.path.join(source_folder, item)
        destination_path = os.path.join(destination_folder, item)

        # Move the file
        os.rename(source_path, destination_path)

print("Practical automation finished")

