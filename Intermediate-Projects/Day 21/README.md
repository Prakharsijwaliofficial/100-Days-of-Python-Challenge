# JSS Snake Game 🐍

A classic arcade-style Snake Game built entirely in Python using the `turtle` graphics library. Navigate the grid, eat food to grow longer, and try to achieve the highest score without crashing!

---

## 🚀 Features

* **Classic Controls:** Smooth grid-based movement using your arrow keys.
* **Dynamic Scoring:** Keeps track of your current score live at the top of the screen.
* **Tail Extension:** The snake grows longer every time it successfully eats food.
* **Collision Detection:** Auto-detects collisions with both the arena walls and the snake's own tail.

---

## 🛠️ Code Architecture

The project is structured across four modular object-oriented components:
1. `main.py` - Sets up the game window, handles keyboard listeners, and manages the primary game loop.
2. `snake.py` - Controls snake generation, segment extensions, and direction changes.
3. `food.py` - Spawns and randomly refreshes food targets on the screen.
4. `scoreboard.py` - Tracks structural text, game score increments, and displays the "Game Over" prompt.

---

## ⚙️ Installation & Setup

### Prerequisites
Make sure you have **Python 3.x** installed on your system. The `turtle` module comes pre-installed with Python standard libraries.

### 1. Clone the Repository
```bash
git clone https://github.com
cd YOUR-REPOSITORY-NAME
```

### 2. Run the Game
Execute the main script to start playing:
```bash
python main.py
```

---

## 🎮 How To Play

Use your standard keyboard arrow keys to guide the snake:
* **Up Arrow** (`↑`) - Move North
* **Down Arrow** (`↓`) - Move South
* **Left Arrow** (`←`) - Move West
* **Right Arrow** (`→`) - Move East

### Game Rules
* Eat food to grow your snake and increase your score.
* The game ends immediately if you hit any of the **four borders** ($600 \times 600$ viewport).
* The game also ends if you turn into or collide with your own **tail segments**.
