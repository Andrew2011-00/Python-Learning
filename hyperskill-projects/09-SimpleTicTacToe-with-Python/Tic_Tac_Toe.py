winning_combinations = [
    [0, 1, 2],  # top row
    [3, 4, 5],  # middle row
    [6, 7, 8],  # bottom row
    [0, 3, 6],  # left column
    [1, 4, 7],  # middle column
    [2, 5, 8],  # right column
    [0, 4, 8],  # diagonal top-left to bottom-right
    [2, 4, 6]   # diagonal top-right to bottom-left
]
def board(grid): # main board
    print("---------")
    print(f"| {grid[0]} {grid[1]} {grid[2]} |")
    print(f"| {grid[3]} {grid[4]} {grid[5]} |")
    print(f"| {grid[6]} {grid[7]} {grid[8]} |")
    print("---------")

player = "X"
game_board = [' ' for _ in range(9)]
board(game_board) # to create an empty board

while True:
        try:
            row_col = input().split()
            row, col = int(row_col[0]), int(row_col[1])
            if not (1 <= row <= 3 and 1 <= col <= 3):
                print("Coordinates should be from 1 to 3!")
                continue
        except (ValueError, IndexError):
            print("You should enter numbers!")
            continue

        index = (row - 1) * 3 + (col - 1)
        if game_board[index] != " ":
            print("This cell is occupied! Choose another one!")
            continue

        game_board[index] = player
        board(game_board)

        for combo in winning_combinations:
            if game_board[combo[0]] == game_board[combo[1]] == game_board[combo[2]] == player:
                print(f"{player} wins")
                exit()

        if ' ' not in game_board:
            print("Draw")
            break

        player = "O" if player == "X" else "X"