# Day 17: The Quiz Game Project

A text-based trivia quiz game built using Python and Object-Oriented Programming (OOP) principles. This project focuses on creating custom classes, initializing attributes, and writing methods to manage game state.

## 🚀 Features
* **Dynamic Question Bank:** Uses a modular data structure (`data.py`) containing true/false questions.
* **Object-Oriented Architecture:** Implements distinct classes for managing questions and the quiz logic.
* **Score Tracking:** Tracks the user's current score and provides instant feedback after each answer.
* **Game Over Summary:** Displays the final score once all questions are answered.

## 📂 Project Structure
* `main.py`: The entry point that initializes the game loop.
* `question_model.py`: Defines the `Question` class with `text` and `answer` attributes.
* `quiz_brain.py`: Contains the `QuizBrain` class managing game state, scoring, and question progression.
* `data.py`: Holds the raw question data array.

## 🛠️ How to Run
1. Clone this repository or navigate to the `Day 17` directory.
2. Open your terminal and run:
   ```bash
   python main.py
   ```
3. Follow the on-screen prompts by typing `True` or `False`.

## 🧠 Concepts Learned
* Creating custom Python classes.
* The `__init__()` constructor method and attribute initialization.
* Designing methods to alter object states.
* Using a list of objects to manage complex data structures.
