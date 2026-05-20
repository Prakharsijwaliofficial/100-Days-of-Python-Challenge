# Day 14: Higher or Lower Game

A command-line guessing game where players compare the Instagram follower counts of famous personalities and brands.

## 🚀 Project Overview

The objective of the game is to correctly guess who has more followers between two choices: **Account A** or **Account B**. 
* If you guess correctly, your score increases, and the winner becomes the new **Account A** for the next round.
* If you guess incorrectly, the game ends immediately, and your final score is displayed.

## 🛠️ What I Learned

* **Game Logic:** Implementing continuous conditional loops (`while` loops) for persistent gameplay.
* **Data Management:** Accessing, reading, and manipulating dictionaries nested inside data lists.
* **Module Reusability:** Importing and using external python assets (ASCII art and data matrices).
* **State Updates:** Shifting data dynamically between variables (`Person B` becoming `Person A`) upon successful conditions.

## 🎮 How to Run

1. Make sure you have Python installed on your machine.
2. Ensure you have the supporting files in the same directory:
   * `main.py` (The core game code)
   * `game_data.py` (The dictionary list containing personalities and follower counts)
   * `art.py` (The ASCII logos and visuals)
3. Run the script via your terminal:
   ```bash
   python main.py
   ```
