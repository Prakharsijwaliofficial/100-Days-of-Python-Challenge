"""
====================================================
           DAY 26 - PYTHON REVISION NOTES
            (Angela Yu - 100 Days of Code)
====================================================

Topics Covered:
1. List Comprehension
2. Dictionary Comprehension
3. Conditional Comprehensions
4. Reading CSV with Pandas
5. DataFrames
6. iterrows()
7. Dictionary from a DataFrame
8. List from User Input
====================================================
"""

import pandas as pd

# ==================================================
# 1. LIST COMPREHENSION
# ==================================================

print("\n========== LIST COMPREHENSION ==========\n")

numbers = [1, 2, 3]

# Create a new list by multiplying each number by 2
new_numbers = [number * 2 for number in numbers]

print("Original List :", numbers)
print("New List      :", new_numbers)

# --------------------------------------------------

name = "Angela"

# Convert every character into a list
letters = [letter for letter in name]

print("\nLetters in Name:", letters)

# --------------------------------------------------

# Create numbers from 1 to 10
range_list = [num for num in range(1, 11)]

print("\nRange List:", range_list)

# ==================================================
# 2. CONDITIONAL LIST COMPREHENSION
# ==================================================

print("\n========== CONDITIONAL LIST COMPREHENSION ==========\n")

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor"]

# Names with length less than 5
short_names = [name for name in names if len(name) < 5]

print("Short Names:", short_names)

# Convert names with length greater than 5 to uppercase
long_names = [name.upper() for name in names if len(name) > 5]

print("Long Names :", long_names)

# ==================================================
# 3. DICTIONARY COMPREHENSION
# ==================================================

print("\n========== DICTIONARY COMPREHENSION ==========\n")

students = ["Alex", "Beth", "Caroline", "Dave"]

# Create random scores
import random

student_scores = {
    student: random.randint(50, 100)
    for student in students
}

print(student_scores)

# ==================================================
# 4. CONDITIONAL DICTIONARY COMPREHENSION
# ==================================================

print("\n========== CONDITIONAL DICTIONARY ==========\n")

passed_students = {
    student: score
    for (student, score) in student_scores.items()
    if score >= 60
}

print("Passed Students:")
print(passed_students)

# ==================================================
# 5. PANDAS DATAFRAME
# ==================================================

print("\n========== PANDAS DATAFRAME ==========\n")

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

data = pd.DataFrame(student_dict)

print(data)

# ==================================================
# 6. ITERROWS()
# ==================================================

print("\n========== ITERROWS() ==========\n")

for (index, row) in data.iterrows():
    print(f"Index : {index}")
    print(f"Student : {row.student}")
    print(f"Score   : {row.score}")
    print()

# ==================================================
# 7. DATAFRAME TO DICTIONARY
# ==================================================

print("\n========== DATAFRAME TO DICTIONARY ==========\n")

nato_example = pd.DataFrame({
    "letter": ["A", "B", "C"],
    "code": ["Alfa", "Bravo", "Charlie"]
})

nato_dict = {
    row.letter: row.code
    for (index, row) in nato_example.iterrows()
}

print(nato_dict)

# ==================================================
# 8. LIST COMPREHENSION WITH USER INPUT
# ==================================================

print("\n========== USER INPUT EXAMPLE ==========\n")

word = input("Enter a word: ").upper()

output = [
    nato_dict[letter]
    for letter in word
    if letter in nato_dict
]

print(output)

# ==================================================
# DAY 26 SUMMARY
# ==================================================

"""
Syntax Learned:

1. List Comprehension
[new_item for item in iterable]

2. List Comprehension with Condition
[new_item for item in iterable if condition]

3. Dictionary Comprehension
{key:value for item in iterable}

4. Dictionary Comprehension with Condition
{key:value for item in iterable if condition}

5. Loop through Dictionary
for key, value in dictionary.items():

6. Loop through DataFrame
for index, row in dataframe.iterrows():

7. Access DataFrame Row
row.column_name

8. DataFrame → Dictionary
{
    row.column1: row.column2
    for (index, row) in dataframe.iterrows()
}

9. Read CSV
pd.read_csv("file.csv")
"""
