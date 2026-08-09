# 🇫🇷 Flashy — Day 31

A **French-English Flash Card App** built with Python and Tkinter as part of **Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**.

The app displays a random French word, automatically flips the card after 3 seconds to reveal the English translation, and allows the user to mark words they already know.

---

## 🚀 Features

* 🎴 Flash card UI built with Tkinter
* 🇫🇷 Displays a random French word
* 🇬🇧 Automatically reveals the English translation after 3 seconds
* ❌ Wrong button → keeps the word in the learning list
* ✅ Right button → removes the known word
* 💾 Saves remaining words to `words_to_learn.csv`
* 🔄 Remembers learning progress between sessions
* 📊 Uses Pandas to read and write CSV files
* 🎲 Uses Python's `random` module to select cards

---

## 🛠️ Technologies Used

* **Python**
* **Tkinter** — GUI development
* **Pandas** — CSV/data handling
* **Random** — Random card selection

---

## 📂 Project Structure

```text
Day 31 - Flash Card Project/
│
├── main.py
│
├── data/
│   ├── french_words.csv
│   └── words_to_learn.csv
│
└── images/
    ├── card_front.png
    ├── card_back.png
    ├── right.png
    └── wrong.png
```

---

## 🧠 How It Works

### 1. Load the vocabulary

The program first tries to load the saved learning list:

```python
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
```

If `words_to_learn.csv` doesn't exist, the original vocabulary file is loaded.

---

### 2. Convert the data

The Pandas DataFrame is converted into a list of dictionaries:

```python
to_learn = data.to_dict(orient="records")
```

Example:

```python
[
    {"French": "chat", "English": "cat"},
    {"French": "chien", "English": "dog"}
]
```

---

### 3. Choose a random card

```python
current_card = random.choice(to_learn)
```

A random card is selected from the learning list.

---

### 4. Display the French word

The Canvas is updated using `itemconfig()`:

```python
canvas.itemconfig(
    word_text,
    text=current_card["French"]
)
```

---

### 5. Automatically flip the card

Tkinter's `after()` method waits for 3 seconds:

```python
window.after(3000, flip_card)
```

Then the card changes to the English side.

---

### 6. Remove known words

When the user clicks the ✅ button:

```python
to_learn.remove(current_card)
```

The known card is removed from the learning list.

---

### 7. Save progress

The remaining words are saved:

```python
pd.DataFrame(to_learn).to_csv(
    "data/words_to_learn.csv",
    index=False
)
```

This means the user's progress is preserved even after closing the application.

---

## 🎯 Key Concepts Learned

This project helped me practice:

* Tkinter GUI development
* Canvas widgets
* `Canvas.create_image()`
* `Canvas.create_text()`
* `Canvas.itemconfig()`
* Tkinter `Button`
* Button `command`
* Functions and callbacks
* `window.after()`
* Pandas DataFrames
* Reading CSV files
* Writing CSV files
* `to_dict(orient="records")`
* Lists of dictionaries
* `random.choice()`
* `try` / `except`
* File persistence
* Global variables

---

## 💡 Important Python Concepts

### Canvas IDs

When creating Canvas objects:

```python
word_text = canvas.create_text(...)
```

Tkinter returns an ID that can later be used:

```python
canvas.itemconfig(word_text, text="Bonjour")
```

---

### Button Commands

```python
Button(command=random_french_word)
```

The function is passed **without parentheses** so Tkinter can call it when the button is clicked.

---

### `after()`

```python
window.after(3000, flip_card)
```

Means:

> Wait 3 seconds, then run `flip_card()`.

---

## 📸 Project

The final application provides a simple interface for learning French vocabulary using flash cards.

---

## 📚 Course

**100 Days of Code: The Complete Python Pro Bootcamp**

Instructor: **Angela Yu**

**Day 31 — Flash Card App**

---

## 🔥 Progress

**Day 31 / 100 Days of Python**

Continuing to build my Python skills through practical projects.
