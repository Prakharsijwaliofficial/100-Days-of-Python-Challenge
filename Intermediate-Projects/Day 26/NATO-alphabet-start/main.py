import pandas as pd
import os

# Get the directory where this Python file (main.py) is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Name of the CSV file
filename = "nato_phonetic_alphabet.csv"

# Create the full path to the CSV file
# This allows the program to find the file regardless of where it is run from
file_path = os.path.join(script_dir, filename)

# Read the CSV file into a Pandas DataFrame
data = pd.read_csv(file_path)

# Create a dictionary:
# Key   -> Letter (A, B, C, ...)
# Value -> NATO code word (Alfa, Bravo, Charlie, ...)
nato_dict = {
    row.letter: row.code
    for (index, row) in data.iterrows()
}

# Ask the user to enter a word
# Convert it to uppercase because our dictionary uses uppercase letters
user_word = input("Enter a word: ").upper()

# Create a list of NATO code words for each letter in the user's word
output_list = [
    nato_dict[letter]
    for letter in user_word
]

# Display the final list
print(output_list)
