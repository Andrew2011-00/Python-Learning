# Simple Tic-Tac-Toe in Python 🎮

This is a basic command-line Tic-Tac-Toe game built in Python as part of the **JetBrains Hyperskill Python Developer track**.  
It helped me understand Python lists, loops, input handling, and how to implement simple game logic.

## 🧠 What I Learned
I struggled a bit with the logic and how to work with lists at first, but I pushed through and got everything working.

Some key things I learned:
- How to create and print a game board using a list
- Mapping 2D input (rows and columns) into a 1D list
- Validating user input to handle errors
- Switching turns between players (`X` and `O`)
- Checking for winning combinations and draw conditions

## 🛠️ How It Works
- The board is a list of 9 elements representing a 3×3 grid.
- Players enter coordinates from 1 to 3 (like a matrix).
- The game checks for:
  - Valid input (numbers, within range)
  - Occupied cells
  - Winning combinations
  - Draw (no empty spaces left)

The game ends when a player wins or there's a draw.
