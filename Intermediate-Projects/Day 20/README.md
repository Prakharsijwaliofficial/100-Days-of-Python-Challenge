# Day 20: Snake Game (Part 1) - Snake Body & Movement

A classic Snake Game built using Python's **Turtle Graphics** module. This project is part of the 100 Days of Code Python Challenge, focusing on Object-Oriented Programming (OOP) principles, event listening, and screen animations.

---

## 🚀 Features

* **Object-Oriented Design**: The snake's behavior and attributes are fully encapsulated within a dedicated `Snake` class.
* **Smooth Animation**: Utilizes Turtle's `tracer()` and `update()` methods to eliminate screen flickering and ensure fluid movement.
* **Keystroke Controls**: Integrates real-time event listeners to control the snake using the arrow keys (`Up`, `Down`, `Left`, `Right`).
* **Directional Logic**: Built-in validation rules to prevent the snake from instantly reversing into itself (e.g., cannot move down while moving up).

---

## 🛠️ Project Structure

```text
Day 20/
├── main.py           # Sets up the game screen, initializes objects, and controls the main game loop.
└── Snake_class.py    # Contains the Snake class responsible for body creation and movement mechanics.
```

---

## ⚙️ Installation & Setup

### Prerequisites
Make sure you have **Python 3.x** installed on your system. The `turtle` module comes pre-installed as part of the Python standard library.

### Running the Game
1. Clone your repository or navigate to your local working directory:
   ```bash
   cd 100-Days-of-Python-Challenge/Intermediate-Projects/Day\ 20
   ```
2. Run the main file using your terminal:
   ```bash
   python main.py
   ```

---

## 🎮 How to Play

* Click on the game window to ensure it is active.
* Use your keyboard **Arrow Keys** to change directions:
  * ⬆️ **Up Arrow**: Move up
  * ⬇️ **Down Arrow**: Move down
  * ⬅️ **Left Arrow**: Move left
  * ➡️ **Right Arrow**: Move right

---

## 🧠 Concepts Learned

* **Class Inheritance & Composition**: Structuring clean, scalable code by breaking game mechanics into objects.
* **Turtle Screen Management**: Refreshing animations at specific intervals using `screen.tracer(0)`.
* **Event Handling**: Binding physical keyboard inputs to execute precise programming methods.
