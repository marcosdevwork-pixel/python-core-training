#==============================================
# EXERCISE 1 - BASIC LIST CREATION
#==============================================

# Create a list to represent file names
file_list = ["download.jpg", "document.txt", "thumb.psd", "book.pdf"]

# Print the list to visualize all files
print(file_list)

# Store each file individually to work with them
first_file = file_list[0]
second_file = file_list[1]
third_file = file_list[2]
fourth_file = file_list[3]

# Print the files individually 
print(first_file)
print(second_file)
print(third_file)
print(fourth_file)

# Print a blank line to separate the output between exercises
print()

#==============================================
# EXERCISE 2 - ITERATING OVER A LIST
#==============================================

# Loop through the file list
for name in file_list:
    # Print each file name
    print(name)

# Print a blank line to separate the output between exercises
print()



#==============================================
# EXERCISE 3 - ADDING FILES TO A LIST
#==============================================

# Create an empty list to store found files
found_files = []

# Add a found file to the list
found_files.append("report1.txt")
found_files.append("image1.jpg")
found_files.append("data.xlsx")
found_files.append("backup.zip")

# Print the list to see all added files
print(found_files)

# Print a blank line to separate the output between exercises
print()

#==============================================
# EXERCISE 4 - REMOVING FILES FROM A LIST
#==============================================

# Create a list of files to simulate files that may need to be removed
files_to_remove = ["report1.txt", "image1.jpg", "data.xlsx", "backup.zip"]

# Remove a file that is no longer needed from the list
files_to_remove.remove("data.xlsx")

# Print the list to see remaining files
print(files_to_remove)

# Print a blank line to separate the output between exercises
print()

#==============================================
# EXERCISE 5 - MODIFYING LIST ITEMS
#==============================================

# Create a list of files to simulate files that need renaming
files_to_rename = ["report_final.txt", "image_old.jpg", "data_2023.xlsx", "backup_old.zip"]

# Print the list to see original file names
print(files_to_rename)

# Update a file name to reflect a new version
files_to_rename[1] = "image_new.jpg"

# Print the list to see updated file names
print(files_to_rename)

# Print a blank line to separate the output between exercises
print()

#==============================================
# EXERCISE 6 - LIST MEMBERSHIP / CHECKING FILES
#==============================================

files_to_check = ["report_final.txt", "image_new.jpg", "data_2023.xlsx", "data_2023.xlsx"]

# Check if the file exists in the list before processing
if "image_new.jpg" in files_to_check:
    print("The file 'image_new.jpg' exists in the list.")
else:
    print("The file 'image_new.jpg' does not exist in the list.")

# Print a blank line to separate the output between exercises
print()

