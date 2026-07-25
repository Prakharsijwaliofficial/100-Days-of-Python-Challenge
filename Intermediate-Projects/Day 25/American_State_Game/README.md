# 🗺️ U.S. States Map Game

An interactive, educational geography game built with Python's **`turtle`** graphics module and **`pandas`** data analysis library. The goal of the game is to test your knowledge of U.S. geography by guessing all 50 states on a blank map.

---

## 🎯 Gameplay Features

* **Interactive Map UI:** Renders a blank map of the United States.
* **Real-time Map Labeling:** Automatically displays state names directly onto their exact $(x, y)$ map coordinates upon correct entry.
* **Input Case Normalization:** Handles user input flexibly (e.g., `"california"`, `"CALIFORNIA"`, or `"cAliFoRnIa"` will all match to `"California"`).
* **Score & Progress Tracking:** Keeps track of how many states you have correctly identified out of 50 in the window title prompt.
* **Study Mode Exit:** Typing `"Exit"` ends the game early and automatically generates a `states_to_learn.csv` file containing every state you missed for review.

---

## 📁 Folder Structure

```text
American_State_Game/
├── 50_states.csv          # CSV dataset containing state names and x, y coordinates
├── blank_states_img.gif   # Graphic background map image
├── main.py                # Main game loop and Turtle rendering logic
└── state_to_learn.py      # Module for exporting missed states to CSV
