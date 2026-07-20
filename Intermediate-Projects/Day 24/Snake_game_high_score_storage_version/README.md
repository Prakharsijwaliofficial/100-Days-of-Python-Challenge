# 🐍 Snake Game - Python Turtle

A classic Snake Game built using **Python** and the **Turtle graphics library**.

The project follows an object-oriented programming (OOP) approach by separating different game components into individual classes like Snake, Food, and Scoreboard.

---

## 🎮 Features

- ✅ Classic Snake gameplay
- ✅ Keyboard controls
- ✅ Snake movement system
- ✅ Random food generation
- ✅ Snake growth after eating food
- ✅ Score tracking system
- ✅ High score saving
- ✅ Wall collision detection
- ✅ Tail collision detection
- ✅ Object-oriented code structure

---

# 📸 Gameplay

The player controls a snake that moves around the screen.

The objective:

- Eat the food 🍎
- Grow longer
- Avoid hitting the walls
- Avoid hitting your own tail
- Achieve the highest score possible

---

# 🛠️ Technologies Used

- **Python 3**
- **Turtle Graphics**
- **Object-Oriented Programming (OOP)**

---

# 📂 Project Structure

```
Snake-Game/
│
├── main.py              # Main game loop and controls
├── snake.py             # Snake class and movement logic
├── food.py              # Food generation system
├── scoreboard.py        # Score and high score management
├── data.txt             # Stores high score
└── README.md            # Project documentation
```

---

# 🎮 Controls

| Key | Action |
|-----|--------|
| ⬆️ Up Arrow | Move Up |
| ⬇️ Down Arrow | Move Down |
| ⬅️ Left Arrow | Move Left |
| ➡️ Right Arrow | Move Right |

---

# 🚀 How To Run

## 1. Clone the repository

```bash
git clone <your-repository-link>
```

## 2. Navigate into the project folder

```bash
cd Snake-Game
```

## 3. Run the game

```bash
python main.py
```

---

# 🧠 Concepts Learned

This project helped practice:

### Python Fundamentals

- Variables
- Functions
- Loops
- Conditional statements
- Lists

### Object-Oriented Programming

- Classes
- Objects
- Inheritance
- Methods
- Constructors (`__init__`)

### File Handling

- Reading and writing files
- Saving high scores permanently

### Game Development Concepts

- Game loops
- Collision detection
- User input handling
- Object movement

---

# ⚙️ How The Game Works

## Snake Movement

The snake consists of multiple turtle objects.

Each segment follows the previous segment:

```
Head → Segment 1 → Segment 2 → Segment 3
```

The snake moves continuously using the game loop.

---

## Food Collision

When:

```python
snake.head.distance(food) < 15
```

The game:

1. Generates new food location
2. Extends the snake length
3. Increases the score

---

## Wall Collision

The game checks if the snake reaches the boundary:

```python
x > 280 or x < -280
y > 280 or y < -280
```

If collision happens:

- Score resets
- Snake starts again

---

## Tail Collision

The game checks if the snake head touches any body segment.

If:

```python
snake.head.distance(segment) < 10
```

The game resets.

---

# 📈 Future Improvements

Possible upgrades:

- Add difficulty levels
- Add pause/resume button
- Add sound effects
- Add animated food
- Add different game modes
- Add graphical menu system
- Add online leaderboard

---

# 👨‍💻 Author

**Prakhar Singh Sijwali**

Python Developer | Aerospace & Technology Enthusiast

---

# 📜 License

This project is open-source and available for learning purposes.
