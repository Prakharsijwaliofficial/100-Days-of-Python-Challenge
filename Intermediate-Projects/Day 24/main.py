"""
=========================================================
PYTHON FILE INPUT / OUTPUT (FILE I/O) NOTES
Angela Yu - 100 Days of Python - Day 24
=========================================================

File I/O allows Python programs to:
- Read data from files
- Write data into files
- Create new files
- Modify existing files

Common file types:
- .txt  -> Text files
- .csv  -> Spreadsheet data
- .json -> Data storage
- .docx -> Word documents
"""


# =========================================================
# 1. OPENING A FILE
# =========================================================

"""
Syntax:

open(filename, mode)

Modes:

"r" -> Read mode (default)
"w" -> Write mode
"a" -> Append mode

"""

file = open("example.txt", "r")

# Always close manually if not using "with"
file.close()


# =========================================================
# 2. USING WITH OPEN (RECOMMENDED)
# =========================================================

"""
The best way to open files.

Advantages:
- Automatically closes the file
- Prevents errors
- Cleaner code
"""

with open("example.txt") as file:
    contents = file.read()
    print(contents)


# =========================================================
# 3. READING FROM A FILE
# =========================================================

"""
read()

Reads the complete file as one string.
"""

with open("example.txt") as file:
    data = file.read()

print(data)



# =========================================================
# 4. READING LINE BY LINE
# =========================================================

"""
readlines()

Returns every line as an item in a list.
"""

with open("names.txt") as file:
    names = file.readlines()

print(names)


# Output example:

# [
# "Angela\n",
# "Jack\n",
# "Prakhar"
# ]



# =========================================================
# 5. REMOVING NEW LINE USING strip()
# =========================================================

"""
strip()

Removes:
- spaces
- tabs
- newline characters

"""

name = "Prakhar\n"

clean_name = name.strip()

print(clean_name)



# =========================================================
# 6. USING splitlines()
# =========================================================

"""
A cleaner way to get lines without \n
"""

with open("names.txt") as file:
    names = file.read().splitlines()

print(names)


# Output:

# ["Angela", "Jack", "Prakhar"]



# =========================================================
# 7. LIST COMPREHENSION WITH FILES
# =========================================================

"""
Short way of writing loops.

Normal:

clean_names = []

for name in names:
    clean_names.append(name.strip())


Short:

"""

with open("names.txt") as file:
    names = [name.strip() for name in file.readlines()]

print(names)



# =========================================================
# 8. WRITING TO A FILE
# =========================================================

"""
"w" mode:

- Creates file if it does not exist
- Deletes old content if file exists

"""

with open("new_file.txt", "w") as file:
    file.write("Hello Python")


# Result:

# new_file.txt
#
# Hello Python



# =========================================================
# 9. APPENDING TO A FILE
# =========================================================

"""
"a" mode:

Adds content without deleting old data.
"""

with open("new_file.txt", "a") as file:
    file.write("\nI love programming")



# =========================================================
# 10. CREATING CUSTOM FILE NAMES
# =========================================================

"""
Using f-strings we can create dynamic filenames.
"""

name = "Prakhar"

with open(f"{name}.txt", "w") as file:
    file.write("Hello Prakhar")


# Creates:

# Prakhar.txt



# =========================================================
# 11. RELATIVE PATHS
# =========================================================

"""
Relative path:
Starts from current project folder.

Example:

Project:

Day_24/
|
|-- main.py
|
|-- data/
    |
    |-- names.txt


"""

with open("data/names.txt") as file:
    print(file.read())



# =========================================================
# 12. ABSOLUTE PATHS
# =========================================================

"""
Complete location of a file.

Windows example:

C:/Users/name/Desktop/file.txt

"""

# with open(r"C:\Users\name\Desktop\file.txt") as file:
#     print(file.read())



# =========================================================
# 13. STRING REPLACEMENT
# =========================================================

"""
replace(old, new)

Used in Mail Merge project.
"""

letter = "Dear [name]"

letter = letter.replace("[name]", "Prakhar")

print(letter)


# Output:

# Dear Prakhar



# =========================================================
# 14. MAIL MERGE PROJECT LOGIC
# =========================================================

"""
Process:

1. Read names file

2. Read starting letter

3. Loop through names

4. Replace [name]

5. Create new letter

"""

names = ["Angela", "Jack", "Prakhar"]

for name in names:

    letter = "Dear [name], Welcome!"

    new_letter = letter.replace("[name]", name)

    with open(f"letter_for_{name}.txt", "w") as file:
        file.write(new_letter)



# =========================================================
# IMPORTANT DIFFERENCE
# =========================================================

"""
read()
---------
Returns complete file as STRING


readlines()
---------
Returns LIST of lines


splitlines()
---------
Returns LIST without \\n characters


write()
---------
Writes STRING into file


"""


# =========================================================
# FINAL CHEAT SHEET
# =========================================================

"""

READ FILE:

with open("file.txt") as file:
    data = file.read()



WRITE FILE:

with open("file.txt", "w") as file:
    file.write("text")



APPEND:

with open("file.txt", "a") as file:
    file.write("more")



REMOVE NEWLINE:

text.strip()



REPLACE TEXT:

text.replace("old","new")



CREATE CUSTOM FILE:

with open(f"{name}.txt","w") as file:
    file.write(text)



"""


print("File I/O Notes Completed ✅")
