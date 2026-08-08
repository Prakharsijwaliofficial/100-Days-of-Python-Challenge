# 🔐 Day 30 — Password Manager

> **100 Days of Code — Python Bootcamp by Angela Yu**

Day 30 of my **100 Days of Python** journey focused on building a fully functional **Password Manager** using Python and Tkinter.

The project allows users to generate strong random passwords, save website credentials locally in a JSON file, and search for saved passwords through a graphical interface.

---

## 🚀 Project Features

* 🔑 Random password generator
* 🔀 Randomized password characters
* 📋 Automatically copies generated passwords to the clipboard
* 💾 Saves passwords to a JSON file
* 🔍 Searches saved credentials by website
* 🖥️ Tkinter graphical user interface
* ⚠️ Input validation
* 🛡️ Exception handling with `try`, `except`, `else`, and `finally`
* 🗂️ Persistent data storage using JSON

---

## 🧠 Concepts Learned

### 1. Tkinter

Used Tkinter to create the graphical user interface.

Important concepts:

```python
Tk()
Label()
Entry()
Button()
Canvas()
messagebox
.grid()
```

---

### 2. Random Password Generation

Used Python's `random` module:

```python
choice()
randint()
shuffle()
```

Example:

```python
password_letters = [
    choice(letters) for _ in range(randint(8, 10))
]
```

This creates a random number of letters.

---

### 3. List Comprehension

Used list comprehensions to generate password characters efficiently:

```python
password_numbers = [
    choice(numbers) for _ in range(randint(2, 4))
]
```

---

### 4. String Joining

After creating the password list:

```python
password = "".join(password_list)
```

This converts the list of characters into one string.

---

### 5. Clipboard

Used `pyperclip` to automatically copy generated passwords:

```python
pyperclip.copy(password)
```

This makes the generated password immediately available for pasting.

---

# 📁 JSON Data Storage

One of the most important concepts from Day 30 was working with JSON.

### Loading JSON

```python
data = json.load(data_file)
```

Think:

```text
JSON file → Python dictionary
```

### Saving JSON

```python
json.dump(data, data_file, indent=4)
```

Think:

```text
Python dictionary → JSON file
```

---

## 🧩 Dictionary Structure

Saved data follows a nested dictionary structure:

```json
{
    "Google": {
        "email": "example@gmail.com",
        "password": "example123"
    }
}
```

This allows the program to store multiple websites and their corresponding credentials.

---

# 🛠️ Exception Handling

Day 30 also introduced practical use of:

```python
try
except
else
finally
```

### `try`

Attempts to execute code that might cause an error.

### `except`

Handles the error if one occurs.

### `else`

Runs when the `try` block succeeds without an error.

### `finally`

Runs regardless of whether an error occurred.

Example:

```python
try:
    with open("data.json", "r") as data_file:
        data = json.load(data_file)

except FileNotFoundError:
    with open("data.json", "w") as data_file:
        json.dump(new_data, data_file, indent=4)

else:
    data.update(new_data)

finally:
    print("Finished")
```

---

# 🔍 Searching Saved Passwords

The search feature retrieves the website from the Tkinter Entry:

```python
search_object = website_entry.get()
```

Then searches the dictionary:

```python
data_object = data[search_object]
```

The email and password are retrieved using:

```python
email_search = data_object.get("email")
password_search = data_object.get("password")
```

If the website doesn't exist:

```python
except KeyError:
```

handles the error and displays an appropriate message.

---

# 📂 Project Structure

```text
Day 30/
│
├── main.py
├── data.json
├── logo.png
└── README.md
```

> `data.json` stores the saved website credentials.

---

# ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Install the required package

```bash
pip install pyperclip
```

### 3. Run the program

```bash
python main.py
```

---

# 📸 Project

The application provides a simple graphical interface where you can:

1. Enter a website
2. Enter an email/username
3. Generate or enter a password
4. Save the credentials
5. Search for previously saved credentials

---

# 💡 Key Takeaways

Day 30 helped me understand how different Python concepts can work together to create a real application.

### Main concepts:

* Tkinter GUI
* Functions
* Dictionaries
* Nested dictionaries
* JSON
* File handling
* Exception handling
* `try / except / else / finally`
* List comprehensions
* Random password generation
* Clipboard management
* Persistent data storage

---

## ⚠️ Security Note

This project is primarily for **learning Python**.

The passwords are stored in `data.json` as plain text, so this should **not be used as a real secure password manager**.

A production password manager would require proper encryption and secure credential storage.

---

# 📈 100 Days of Python

**Day 30 / 100** ✅

> Building projects. Learning Python. Getting closer to becoming a better developer.

### Next → Day 31 🚀
