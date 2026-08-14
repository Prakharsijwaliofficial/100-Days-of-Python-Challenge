# 💬 Kanye Says...

A simple **Tkinter GUI application** built as part of **Day 33 of Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**.

The application uses the **Kanye REST API** to fetch a random Kanye West quote and displays it on a graphical interface whenever the user clicks the button.

---

## 📌 Project Overview

The application provides a simple graphical interface containing:

* 🖼️ A background image
* 💬 A quote display area
* 🖱️ A button with an image
* 🌐 An API connection to fetch random quotes

Whenever the button is clicked, the program sends a request to the Kanye REST API, receives a random quote, and updates the text displayed on the Canvas.

---

## 🧠 Concepts Practiced

This project helped me practice:

* 🐍 Python
* 🖥️ Tkinter GUI development
* 🎨 Tkinter `Canvas`
* 🖼️ `PhotoImage`
* 🔘 Tkinter `Button`
* 🌐 API requests
* 📦 JSON data
* 🔄 Functions
* 🧩 Updating Canvas elements
* 🖱️ Button commands
* 📐 Tkinter `grid()` layout

---

## 🛠️ Technologies Used

* **Python**
* **Tkinter**
* **Requests**

### API Used

**Kanye REST API**

The API provides random Kanye West quotes in JSON format.

---

## 📂 Project Structure

```text id="9b4k6f"
kanye-says/
│
├── main.py
│
└── Kayne/
    ├── background.png
    └── kanye.png
```

> Note: The folder is named `Kayne` in the current project structure to match the path used in the Python code.

---

## ⚙️ How It Works

### 1. Create the GUI

The application starts by creating a Tkinter window:

```python id="mxq2d3"
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)
```

This creates the main application window.

---

### 2. Create the Canvas

A Canvas is used to display the background and quote:

```python id="0xjq6p"
canvas = Canvas(width=300, height=414)
```

The background image is then placed on the Canvas:

```python id="dd2x5a"
canvas.create_image(150, 207, image=background_img)
```

---

### 3. Display the Quote

The initial quote text is created using:

```python id="x6n4bx"
quote_text = canvas.create_text(
    150,
    207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Arial", 30, "bold"),
    fill="white"
)
```

The important part here is that the returned Canvas item ID is stored in:

```python id="t5j5v9"
quote_text
```

This allows the program to modify the same text later.

---

### 4. Fetch a Random Quote

When the button is clicked, the `get_quote()` function runs:

```python id="5v7d5k"
def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    quote = response.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)
```

The program:

1. Sends a request to the API.
2. Receives JSON data.
3. Extracts the `"quote"` value.
4. Updates the existing Canvas text.

---

### 5. Update the Canvas Text

The key line is:

```python id="1w8e9z"
canvas.itemconfig(quote_text, text=quote)
```

Instead of creating a new text element every time, `itemconfig()` changes the existing Canvas item.

This was an important concept learned in the project.

---

### 6. Create the Button

The Kanye image is used as the button:

```python id="2om7wa"
kanye_button = Button(
    image=kanye_img,
    highlightthickness=0,
    command=get_quote
)
```

The `command=get_quote` means that clicking the button calls the `get_quote()` function.

---

## 🔄 Application Flow

```text id="6jj4xq"
Start Application
       ↓
Create Tkinter Window
       ↓
Display Background
       ↓
Display Initial Text
       ↓
User Clicks Button
       ↓
Request Quote from API
       ↓
Receive JSON Response
       ↓
Extract Quote
       ↓
Update Canvas Text
       ↓
Display New Quote
```

---

## ▶️ How to Run

### 1. Install Requests

If `requests` isn't already installed:

```bash
pip install requests
```

### 2. Make sure the images are in the correct folder

```text id="7hmh2f"
Kayne/
├── background.png
└── kanye.png
```

### 3. Run the program

```bash
python main.py
```

Click the Kanye button to generate a new quote.

---

## 📸 Features

* 🎨 Simple graphical interface
* 🖼️ Custom background and button images
* 🌐 Live API requests
* 💬 Random quote generation
* ⚡ Instant GUI updates
* 🐍 Built entirely with Python

---

## 🚀 Future Improvements

Possible improvements:

* [ ] Add error handling if the API is unavailable.
* [ ] Add a loading indicator while requesting a quote.
* [ ] Add a copy-to-clipboard button.
* [ ] Allow users to save favorite quotes.
* [ ] Improve the GUI design.
* [ ] Add an internet connection check.

---

## 🎓 Course

**100 Days of Code: The Complete Python Pro Bootcamp**

**Day 33 — API Endpoints & API Parameters**

Project: **Kanye Says...**

---

## 👨‍💻 Author

**Prakhar Singh Sijwali**

Built as part of my Python learning journey and **100 Days of Code** challenge.

---

⭐ Part of my ongoing Python development journey.
