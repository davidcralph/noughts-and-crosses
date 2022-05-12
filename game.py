# init
player = {
    1: "X",
    2: "O",
}
board = {
    1: "-",
    2: "-",
    3: "-",
    4: "-",
    5: "-",
    6: "-",
    7: "-",
    8: "-",
    9: "-"
}

print("Welcome to noughts and crosses!")
# func
def render_board():
    print(board[1] + "|" + board[2] + "|" + board[3])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9])

render_board()

def check_win():
    # plyr1
    if board[1] == player[1] and board[2] == player[1] and board[3] == player[1]:
        print("Player 1 wins!")
        return True
    elif board[4] == player[1] and board[5] == player[1] and board[6] == player[1]:
        print("Player 1 wins!")
        return True
    elif board[7] == player[1] and board[8] == player[1] and board[9] == player[1]:
        print("Player 1 wins!")
        return True
    elif board[1] == player[1] and board[4] == player[1] and board[7] == player[1]:
        print("Player 1 wins!")
        return True
    elif board[2] == player[1] and board[5] == player[1] and board[8] == player[1]:
        print("Player 1 wins!")
        return True
    elif board[3] == player[1] and board[6] == player[1] and board[9] == player[1]:
        print("Player 1 wins!")
        return True
    elif board[1] == player[1] and board[5] == player[1] and board[9] == player[1]:
        print("Player 1 wins!")
        return True
    elif board[3] == player[1] and board[5] == player[1] and board[7] == player[1]:
        print("Player 1 wins!")
        return True
    # plyr2
    elif board[1] == player[2] and board[2] == player[2] and board[3] == player[2]:
        print("Player 2 wins!")
        return True
    elif board[4] == player[2] and board[5] == player[2] and board[6] == player[2]:
        print("Player 2 wins!")
        return True
    elif board[7] == player[2] and board[8] == player[2] and board[9] == player[2]:
        print("Player 2 wins!")
        return True
    elif board[1] == player[2] and board[4] == player[2] and board[7] == player[2]:
        print("Player 2 wins!")
        return True
    elif board[2] == player[2] and board[5] == player[2] and board[8] == player[2]:
        print("Player 2 wins!")
        return True
    elif board[3] == player[2] and board[6] == player[2] and board[9] == player[2]:
        print("Player 2 wins!")
        return True
    elif board[1] == player[2] and board[5] == player[2] and board[9] == player[2]:
        print("Player 2 wins!")
        return True
    elif board[3] == player[2] and board[5] == player[2] and board[7] == player[2]:
        print("Player 2 wins!")
        return True
    else:
        return False

def run_turn(num):
    global current
    current = num
    pos = input("Choose a square player " + str(current) + ": ")
    if not pos.isdigit():
        print("Please enter a number.")
        run_turn(current)
    elif int(pos) not in board:
        print("Please enter a number between 1 and 9.")
        run_turn(current)
    elif board[int(pos)] != "-":
        print("Please enter a number that is not already taken.")
        run_turn(current)
    else:
      board[int(pos)] = player[int(num)]
      render_board()
      if check_win() == True:
        return exit()
      if current == "1":
          current = "2"
      else:
          current = "1"
      run_turn(current)
      

# start with p1 might change later
run_turn("1")
