# ✈️ NATO Phonetic Alphabet Project

A simple Python project that converts a word entered by the user into its corresponding **NATO Phonetic Alphabet** code words.

This project was built as part of **Day 26** of **Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**.

---

## 📂 Project Structure

```
NATO_Alphabet_Project/
│
├── main.py
└── nato_phonetic_alphabet.csv
```

### 📄 Files

- **main.py** → Reads the CSV file, creates a NATO dictionary, accepts user input, and prints the phonetic code words.
- **nato_phonetic_alphabet.csv** → Contains the NATO phonetic alphabet data (Letter → Code Word).

---

## 📖 Concepts Practiced

During this project, I learned and practiced:

- ✅ Reading CSV files with **Pandas**
- ✅ Working with **DataFrames**
- ✅ Using **`iterrows()`**
- ✅ Dictionary Comprehensions
- ✅ List Comprehensions
- ✅ Handling user input
- ✅ Working with file paths using the **os** module

---

## ⚙️ How It Works

1. Read the `nato_phonetic_alphabet.csv` file.
2. Convert the CSV data into a Python dictionary.
3. Ask the user to enter a word.
4. Convert the word to uppercase.
5. Find the NATO code word for each letter.
6. Display the final list of code words.

---

## 🔄 Program Flow

```
Read CSV
    │
    ▼
Create DataFrame
    │
    ▼
Create NATO Dictionary
    │
    ▼
Get User Input
    │
    ▼
Convert to Uppercase
    │
    ▼
Find NATO Code Words
    │
    ▼
Display Output
```

---

## 💻 Example

### Input

```text
Enter a word: Hello
```

### Output

```python
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```

---

## 🛠 Technologies Used

- Python 3
- Pandas
- CSV
- os Module

---

## 📚 Key Python Concepts

### Dictionary Comprehension

```python
nato_dict = {
    row.letter: row.code
    for (index, row) in data.iterrows()
}
```

Creates a dictionary where:

- **Key** → Letter (`A`, `B`, `C`, ...)
- **Value** → NATO Code Word (`Alfa`, `Bravo`, `Charlie`, ...)

---

### List Comprehension

```python
output_list = [
    nato_dict[letter]
    for letter in user_word
]
```

Creates a list of NATO code words for every letter entered by the user.

---

## 🎯 Learning Outcome

By completing this project, I gained hands-on experience with:

- Reading and processing CSV files
- Creating dictionaries from structured data
- Using comprehensions to write cleaner Python code
- Working with user input
- Organizing project files using relative file paths

---

## 👨‍💻 Course Information

**Course:** 100 Days of Code – The Complete Python Pro Bootcamp

**Instructor:** Angela Yu

**Day:** 26 – List Comprehensions, Dictionary Comprehensions & Pandas
