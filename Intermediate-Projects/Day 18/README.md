# Day 18: Hirst Painting Generator 🎨

An automated Python script that extracts a color palette from an image using the `colorgram` library and recreates a Damien Hirst-style spot painting using `turtle` graphics.

---

## 🚀 Features

* **Color Extraction:** Programmatically reads an image file to pull out a rich color palette.
* **Smart Filtering:** Automatically filters out bright background colors (whites/creams) to keep the painting vibrant.
* **Dynamic Grid Rendering:** Draws a perfectly aligned 10x10 grid of randomized colorful dots.

---

## 🛠️ Requirements & Installation

This project requires Python 3 and the `colorgram.py` package.

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   ```

2. **Navigate to the project folder:**
   ```bash
   cd 100-Days-of-Python-Challenge/Intermediate-Projects/Day\ 18
   ```

3. **Install dependencies:**
   ```bash
   pip install colorgram.py
   ```

---

## 💻 How It Works

1. Place your target image named `image.jpg` inside your project directory.
2. The script extracts up to 30 unique RGB colors from the image.
3. The `turtle` module sets up a custom canvas window.
4. The turtle painter iterates 100 times to spawn a spot painting grid with 50px spacing.

---

## ⚙️ Configuration

You can easily customize the output by modifying these variables in `main.py`:

```python
dot_size = 20      # Changes the size of the dots
spacing = 50       # Changes the distance between dots
dots_per_row = 10  # Changes grid dimensions
```

