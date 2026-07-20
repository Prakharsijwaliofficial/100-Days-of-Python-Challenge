# ✉️ Mail Merge Project - Python

A Python automation project that creates personalized letters automatically for multiple people using a template letter.

Instead of manually editing hundreds of letters, this program reads names from a file, replaces the placeholder name in a template, and generates customized letters for each person.

---

# 🚀 Features

- ✅ Reads names from a text file
- ✅ Removes unnecessary whitespace using `.strip()`
- ✅ Reads a template letter
- ✅ Replaces `[name]` placeholder automatically
- ✅ Creates personalized letters for every person
- ✅ Saves generated letters automatically
- ✅ Uses file handling and automation concepts

---

# 🛠️ Technologies Used

- Python 3
- File Handling
- String Manipulation
- Loops
- List Comprehension

---

# 📂 Project Structure

```
Mail Merge Project/
│
├── Input/
│   │
│   ├── Names/
│   │   └── invited_names.txt
│   │
│   └── Letters/
│       └── starting_letter.txt
│
├── Output/
│   │
│   └── ReadyToSend/
│       ├── letter_for_Angela.docx
│       ├── letter_for_Jack.docx
│       └── letter_for_Prkahar.docx
│
└── main.py
```

---

# 📄 Input Files

## invited_names.txt

Contains names separated by new lines:

```
Angela
Jack
Prakhar
Alex
```

---

## starting_letter.txt

Template letter:

```
Dear [name],

You are invited to my event.

Hope you can come!

Regards
```

---

# ⚙️ How It Works

## 1. Reading Names

The program opens the names file:

```python
with open("invited_names.txt") as file:
    names = [name.strip() for name in file.readlines()]
```

The `.strip()` method removes the newline character (`\n`) from each name.

Example:

Before:

```python
["Angela\n", "Jack\n"]
```

After:

```python
["Angela", "Jack"]
```

---

## 2. Reading Letter Template

The program loads the starting letter:

```python
draft_mail = file.read()
```

Example:

```
Dear [name],
Welcome!
```

---

## 3. Replacing Placeholder

The placeholder:

```
[name]
```

is replaced with the real person's name.

Example:

Before:

```
Dear [name],
```

After:

```
Dear Angela,
```

Using:

```python
draft_mail.replace("[name]", n)
```

---

## 4. Creating Personalized Letters

For every name, Python creates a new file:

```python
with open(f"letter_for_{n}.docx", "w") as file:
    file.write(mail)
```

Example output:

```
letter_for_Angela.docx
letter_for_Jack.docx
letter_for_Prakhar.docx
```

---

# 🧠 Concepts Practiced

## File Handling

- Opening files
- Reading files
- Writing files
- Creating new files

---

## String Manipulation

- `.replace()`
- `.strip()`

---

## Python Lists

- Reading multiple values
- List comprehension

---

## Automation

The program performs repetitive work automatically:

Manual process:

```
Open letter
Change name
Save file
Repeat 100 times
```

Python process:

```
Run program → 100 personalized letters created
```

---

# ▶️ How To Run

Clone the repository:

```bash
git clone <repository-link>
```

Open the project folder:

```bash
cd Mail-Merge-Project
```

Run:

```bash
python main.py
```

---

# 📈 Future Improvements

Possible upgrades:

- Create real `.docx` files using `python-docx`
- Add email sending functionality
- Add HTML email templates
- Add GUI interface
- Support thousands of recipients
- Add error handling

---

# 👨‍💻 Author

**Prakhar Singh Sijwali**

Python Developer | Aerospace & Technology Enthusiast

---

# 📜 License

This project is created for learning Python automation and programming concepts.
