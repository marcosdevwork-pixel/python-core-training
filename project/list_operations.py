#==============================================
# EXERCISE 1 - ADDING ITEMS TO A LIST
#==============================================

# At the start of the automation, no files were found yet
found_files = []

# The automation finds one specific file
found_files.append("report_january.pdf")

# Show the list after adding one file
print(f"Files found after append: {found_files}")

# The automation finds multiple files at once
more_files = ["image_01.jpg", "notes.txt", "backup.zip"]

# Add all new files to the main list
found_files.extend(more_files)

# Show the list after adding multiple files
print(f"Files found after extend: {found_files}")
print("---------------")

#==============================================
# EXERCISE 2 - REMOVING ITEMS FROM A LIST
#==============================================

# List of files found by the automation
files = ["image_01.jpg", "notes.txt", "backup.zip"]

# Show the original list
print(f"The original file list: {files}")

# Remove a specific file by name
files.remove("notes.txt")

# Show the list after removing the file
print(f"The list after removing the file: {files}")

# Remove the first file from the list (by position)
processed_file = files.pop(0)

# Show the file that was removed
print(f"Processed file: {processed_file}")

# Show the list after pop
print(f"Remaining files: {files}")

# Remove the last file using del
del files[-1]

# Show the final state of the list
print(f"Final file list: {files}")
print("---------------")

#==============================================
# EXERCISE 3 - COPYING LISTS SAFELY
#==============================================

# WRONG copy
original_files = ["image_01.jpg", "notes.txt", "backup.zip"]

print(f"Original files: {original_files}")

files_to_process = original_files

files_to_process.remove("notes.txt")

print(f"Files to process: {files_to_process}")
print(f"Original files: {original_files}")

# Correct copy (RESET original list)
original_files = ["image_01.jpg", "notes.txt", "backup.zip"]

files_to_process = original_files.copy()
files_to_process.remove("notes.txt")

print(f"Files to process (safe): {files_to_process}")
print(f"Original files (unchanged): {original_files}")
print("---------------")

#==============================================
# EXERCISE 4 - CHECKING ITEMS IN A LIST
#==============================================

# List of files found by the automation
files = ["image_01.jpg", "notes.txt", "backup.zip"]

# File that the automation wants to check
file_to_check = "notes.txt"

# Check if the file exists in the list
if file_to_check in files:
   # Store the result as True if the file is found
   file_exists = True
else:
   # Store the result as False if the file is not found
   file_exists = False

# Show the result of the check
print(f"File exists? {file_exists}")
print("---------------")

#==============================================
# EXERCISE 5 - ITERATING WITH CONTROL
#==============================================

# List for files found by the automation
files = ["image_01.jpg", "notes.txt", "backup.zip", "presentation.pdf"]

# List of the extensions tha shound be skipped
skip_extensions = [".txt", ".zip"]

# First loop: print all files
for file in files:
   print(file)
print("---------------")

# Second loop: print only files that are not in the skip list
for file in files:

   # Check if the file ends with any extension in the skip list
   if any(file.endswith(ext) for ext in skip_extensions):

      continue # Skip this file and continue with the next one

   # Show the file  that passed the check
   print(file)
print("---------------")

#==============================================
# EXERCISE 6 - CLEARING A LIST
#==============================================

# List of the files that were processed by the automation
processed_files = ["import.pdf", "image.jpg", "backup.zip"]

# Show the list before the clearing
print(f"Files before clearing: {processed_files}")

# Clear the list after processed
processed_files.clear()

# Show the list after the clearing
print(f"Files after clearing: {processed_files}")