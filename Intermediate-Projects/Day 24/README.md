# 🐍 Day 24 - Python File I/O, Mail Merge & Snake Game

## Angela Yu - 100 Days of Python Bootcamp

This folder contains all the concepts, notes, and projects completed during **Day 24** of Angela Yu's **100 Days of Code: The Complete Python Pro Bootcamp**.

The main topic of this day was **File Input and Output (File I/O)**, where we learned how Python can interact with files by reading, writing, creating, and modifying data.

Along with File I/O concepts, this day also included practical automation and game development projects.

---

# 📚 Topics Covered

## 📂 File Input / Output (File I/O)

The root `main.py` file contains complete notes and examples about File I/O.

Topics covered:

- Opening files
- Reading files
- Writing files
- Appending data
- Creating new files
- File paths
- Relative paths
- Absolute paths
- String replacement
- Removing extra characters
- List comprehension
- Dynamic file creation

---

# 📖 File Reading

Python can read data from files using:

```python
with open("file.txt") as file:
    data = file.read()
```

---

## read()

Reads the complete file as a string.

Example:

```python
contents = file.read()
```

---

## readlines()

Reads every line and stores them as a list.

Example:

```python
names = file.readlines()
```

Output:

```python
[
"Angela\n",
"Jack\n",
"Prakhar"
]
```

---

## splitlines()

A cleaner way to get lines without newline characters.

Example:

```python
names = file.read().splitlines()
```

Output:

```python
[
"Angela",
"Jack",
"Prakhar"
]
```

---

# ✨ String Cleaning

## strip()

Removes unnecessary characters from the beginning and end of a string.

Removes:

- Spaces
- New lines (`\n`)
- Tabs (`\t`)

Example:

```python
name = "Prakhar\n"

name.strip()
```

Output:

```
Prakhar
```

---

# ✏️ Writing Files

Python can create and write files using:

```python
with open("file.txt","w") as file:
    file.write("Hello")
```

## Write Mode (`w`)

- Creates a file if it does not exist
- Replaces old content

---

# ➕ Append Mode

Used to add new content without deleting old content.

```python
with open("file.txt","a") as file:
    file.write("New data")
```

---

# 📍 File Paths

## Relative Path

Path based on the current project location.

Example:

```
Project
│
├── main.py
│
└── data
    └── file.txt
```

Code:

```python
open("data/file.txt")
```

---

## Absolute Path

Complete location of a file.

Example:

```python
open(r"C:\Users\User\Desktop\file.txt")
```

---

# 🔄 String Replacement

Using:

```python
replace()
```

Example:

```python
text.replace("[name]", "Prakhar")
```

Before:

```
Dear [name]
```

After:

```
Dear Prakhar
```

---

# 📧 Project 1 - Mail Merge Automation

## Description

A Python automation project that creates personalized letters automatically.

Instead of manually changing names in every letter, Python reads names from a file and generates customized letters.

---

# ⚙️ How It Works

The program:

1. Reads names from `invited_names.txt`
2. Reads the letter template
3. Replaces `[name]` with actual names
4. Creates separate letters automatically

---

# Project Structure

```
Mail Merge Project

│
├── main.py
│
├── Input
│   │
│   ├── Names
│   │   └── invited_names.txt
│   │
│   └── Letters
│       └── starting_letter.txt
│
└── Output
    └── ReadyToSend
        ├── letter_for_Angela.docx
        ├── letter_for_Jack.docx
        └── letter_for_Prakhar.docx
```

---

# Concepts Used

- File reading
- File writing
- Loops
- Lists
- List comprehension
- String replacement
- Dynamic filenames

---

# 🐍 Project 2 - Snake Game

## Description

A classic Snake Game built using Python Turtle graphics and Object-Oriented Programming.

The game includes movement, food collection, scoring, and collision detection.

---

# Features

✅ Snake movement

✅ Keyboard controls

✅ Food generation

✅ Snake growth

✅ Score system

✅ High score saving

✅ Wall collision detection

✅ Tail collision detection

---

# Snake Game Structure

```
Snake Game

│
├── main.py
│
├── snake.py
│
├── food.py
│
├── scoreboard.py
│
└── data.txt
```

---

# OOP Concepts Used

## Classes

Created separate classes:

```python
Snake()
Food()
Scoreboard()
```

---

## Objects

Objects are created in `main.py`:

```python
snake = Snake()

food = Food()

scoreboard = Scoreboard()
```

---

# Game Loop

The game continuously runs using:

```python
while game_is_on:
```

The loop handles:

- Screen updates
- Snake movement
- Food collision
- Wall collision
- Tail collision
- Score updates

---

# 🧠 Skills Learned

During Day 24, I practiced:

## Python Programming

- File handling
- Data processing
- Automation
- String manipulation

## Programming Concepts

- Lists
- Loops
- Functions
- Classes
- Objects
- Project organization

## Real-World Applications

File I/O is used in:

- Saving game progress
- Creating reports
- Generating documents
- Data processing
- Automation scripts

---

# 📁 Complete Folder Structure

```
Day_24-

│
├── main.py
│   |
│   └── File I/O Notes
│
├── Mail Merge Project
│   |
│   └── main.py
│
├── Snake Game
│   |
│   ├── main.py
│   ├── snake.py
│   ├── food.py
│   ├── scoreboard.py
│   └── data.txt
│
└── README.md
```

---

# 👨‍💻 Author

**Prakhar Singh Sijwali**

Python Developer | Aerospace & Technology Enthusiast

---

# 🎓 Course

Angela Yu  
**100 Days of Code: The Complete Python Pro Bootcamp**

## Day 24 Completed ✅
