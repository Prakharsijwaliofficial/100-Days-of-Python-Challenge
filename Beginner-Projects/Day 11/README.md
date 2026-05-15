# Day 11 - Blackjack Game 🃏🐍

A command-line text-based simulation of the classic casino game **Blackjack** (also known as 21). This project is part of Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.

---

## 🎯 Project Overview
The game follows simplified casino rules where a user plays against an automated dealer (the computer). The goal is to get a hand value closer to 21 than the dealer without going over (busting).

### 🛠️ Features
- **Dynamic Scoring**: Automatically tracks and calculates hand totals.
- **Smart Ace Handling**: Dynamically changes the value of an Ace from 11 to 1 if the player's score exceeds 21.
- **Automated Dealer AI**: The computer automatically hits until its card value reaches a minimum of 17.
- **Game Loop**: Option to endlessly replay matches without restarting the program.
- **ASCII Art**: Includes custom visual branding layouts using an `art.py` file module.

---

## 🧠 What I Learned
- Structuring nested **`while` and `if/elif/else` loops** to handle complex game states.
- List indexing techniques using `.index()` to modify active list elements.
- Tracking program boolean state flags (`player_drawing = True`) to safely enter and break out of inner loops.
- Importing internal modules and variables across separate project files.

---

## 🚀 How to Run

1. Make sure you have Python installed on your system.
2. Clone this repository or download the project files.
3. Ensure both `main.py` and `art.py` are saved in the same directory.
4. Run the program using your terminal or favorite IDE:
   ```bash
   python main.py
   ```

---

## 📜 Game Rules Used
- The deck is infinite (cards are picked randomly with replacement).
- The Jack, Queen, and King cards count as a value of `10`.
- The Ace counts as `11` or `1` depending on the current score threshold.
- The player goes first and can choose to **Hit** (`'y'`) to take another card, or **Pass** (`'n'`) to lock in their score.
- The dealer must continue drawing cards if their total hand value is strictly under `17`.
