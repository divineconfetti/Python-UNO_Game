# 🃏 Python UNO Game

A fully playable, terminal-based UNO game built entirely in Python. Play a rule-accurate game against a dynamic, automated AI opponent directly in your command line!

## ✨ Features
* **Object-Oriented Design:** Built from scratch using custom Python classes for Cards, Decks, and Players.
* **Automated AI Opponent:** A dynamic computer player that scans its hand, plays valid matches, and draws when trapped.
* **Full Action Card Logic:** Fully functional Skip, Reverse, `+2`, and `+4` cards that force the opponent to lose turns or draw cards. *(Note: In this 2-player version, Skip and Reverse both grant the player an extra turn!)*
* **Dynamic Wild Cards:** Color-changing logic that actively updates the table state and forces the next player to match the new color.
* **Draw-and-Play Mechanic:** If you draw a card that matches the table, you are immediately given the option to play it.
* **"UNO!" Tracking:** The game automatically tracks hand sizes and yells "UNO!" when either player drops to a single card.

## 🚀 How to Play

### Prerequisites
You must have Python 3 installed on your computer. No external libraries are required!

### Running the Game
1. Clone this repository or download the `uno.py` file to your machine.
2. Open your terminal or command prompt.
3. Navigate to the folder containing the file.
4. Run the following command:
   ```bash
   python uno.py
