# Day 19: Intermediate Python Projects

Welcome to Day 19 of the **100 Days of Python Challenge**! This directory contains two interactive graphical projects built using Python's built-in `turtle` module. 

## 📁 Repository Structure

*   `Etch-a-Sketch-app.py`: A classic drawing app controlled by keyboard key presses.
*   `Turtle-racing-game.py`: A complete turtle racing game featuring random movement mechanics and an interactive betting system.

---

## 🎮 Projects Overview

### 1. Etch-a-Sketch App (`Etch-a-Sketch-app.py`)
Recreate the classic childhood drawing toy right on your screen. Use event listeners to bind custom drawing actions directly to your keyboard.

*   **Controls:**
    *   `W`: Move Forward
    *   `S`: Move Backward
    *   `A`: Turn Counter-Clockwise (Left)
    *   `D`: Turn Clockwise (Right)
    *   `C`: Clear the screen and reset the turtle pointer position

### 2. Turtle Racing Game (`Turtle-racing-game.py`)
An interactive betting game where 6 distinctly colored turtles compete on a digital track.

*   **Features:**
    *   **Interactive Input:** A pop-up prompt allows users to type in their bet on a specific color before the race starts.
    *   **Dynamic Positioning:** Automatically lines up all 6 turtles parallel at the starting gate.
    *   **Randomized Mechanics:** Employs the `random` module to step turtles forward unpredictably.
    *   **Win/Loss Output:** Checks coordinates dynamically to instantly announce if your color crossed the finish line first.

---

## 🛠️ How to Run

1. Make sure you have **Python 3.x** installed on your system.
2. Clone this repository or navigate directly to your Day 19 project directory.
3. Execute either script using your terminal or favorite IDE (e.g., PyCharm):

```bash
python Turtle-racing-game.py
```

## 📝 Concepts Learned
*   Python Turtle Graphics (Coordinates, Colors, Shapes)
*   Higher-Order Functions and passing functions as arguments
*   Turtle Event Listeners (`screen.listen()`, `screen.onkey()`)
*   Object-Oriented Programming (Creating multiple independent Object instances from a Single Class)
*   Using While Loops for real-time game state tracking
