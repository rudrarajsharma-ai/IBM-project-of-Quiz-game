# Python Quiz Portal

## Project Overview
The Python Quiz Portal is a simple, console-based application built using core Python. It tests the user’s knowledge of basic Python programming through 10 multiple-choice questions, calculates their final score and accuracy, and saves the results to a text file.

## Features
* **Interactive Gameplay:** Takes the player's name and asks 10 multiple-choice questions one by one.
* **Instant Feedback:** Tells the player immediately whether their selected answer is right or wrong.
* **Score Report:** Displays total questions, right answers, wrong answers, total points, and percentage at the end of the quiz.
* **Score Saving:** Automatically saves each player's final report into a `scores.txt` file.

## Concepts Used
* **Basics & Strings:** `input()`, `print()`, string formatting (f-strings), `.strip()`, `.upper()`, and basic arithmetic operations.
* **Control Flow & Functions:** `for` loop, `while` loop, `if-else` conditions, and modular functions (`start_quiz()`, `save_score()`).
* **Data Structures:** Lists, Dictionaries (for storing questions and answers), Tuples (for options), and Sets (for displaying quiz topics).
* **Files, Exceptions & OOP:** `Player` class and object creation (`__init__`), file handling (with `open()`), and exception handling (`try-except`).

## How to Run the Project
1. Make sure Python 3 is installed on your computer.
2. Save the code in a file named `quiz.py`.
3. Open your terminal or command prompt in the project folder and run:
   ```bash
   python quiz.py
