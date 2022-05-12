from colorama import init, Fore, Back, Style
from emoji import emojize

# init
init() # this is for terminal colors, yes
player = {
    1: Fore.RED + "X" + Style.RESET_ALL,
    2: Fore.YELLOW + "O" + Style.RESET_ALL,
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

print(Fore.BLUE + "Welcome to " + Fore.RED + "noughts " + Fore.BLUE + "and " + Fore.YELLOW + "crosses" + Fore.BLUE + "!" + Style.RESET_ALL)
print(Fore.GREEN + "Written by David Ralph " + Style.RESET_ALL + emojize(":eyes:"))
# func
def render_board():
    print(board[1] + "|" + board[2] + "|" + board[3])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9])

render_board()

def check_win():
    # plyr1
    if board[1] == player[1] and board[2] == player[1] and board[3] == player[1]:
        print("Player 1 wins! " + emojize(":party_popper:"))
        return True
    elif board[4] == player[1] and board[5] == player[1] and board[6] == player[1]:
        print("Player 1 wins! " + emojize(":party_popper:"))
        return True
    elif board[7] == player[1] and board[8] == player[1] and board[9] == player[1]:
        print("Player 1 wins! " + emojize(":party_popper:"))
        return True
    elif board[1] == player[1] and board[4] == player[1] and board[7] == player[1]:
        print("Player 1 wins! " + emojize(":party_popper:"))
        return True
    elif board[2] == player[1] and board[5] == player[1] and board[8] == player[1]:
        print("Player 1 wins! " + emojize(":party_popper:"))
        return True
    elif board[3] == player[1] and board[6] == player[1] and board[9] == player[1]:
        print("Player 1 wins! " + emojize(":party_popper:"))
        return True
    elif board[1] == player[1] and board[5] == player[1] and board[9] == player[1]:
        print("Player 1 wins! " + emojize(":party_popper:"))
        return True
    elif board[3] == player[1] and board[5] == player[1] and board[7] == player[1]:
        print("Player 1 wins! " + emojize(":party_popper:"))
        return True
    # plyr2
    elif board[1] == player[2] and board[2] == player[2] and board[3] == player[2]:
        print("Player 2 wins! " + emojize(":party_popper:"))
        return True
    elif board[4] == player[2] and board[5] == player[2] and board[6] == player[2]:
        print("Player 2 wins! " + emojize(":party_popper:"))
        return True
    elif board[7] == player[2] and board[8] == player[2] and board[9] == player[2]:
        print("Player 2 wins! " + emojize(":party_popper:"))
        return True
    elif board[1] == player[2] and board[4] == player[2] and board[7] == player[2]:
        print("Player 2 wins! " + emojize(":party_popper:"))
        return True
    elif board[2] == player[2] and board[5] == player[2] and board[8] == player[2]:
        print("Player 2 wins! " + emojize(":party_popper:"))
        return True
    elif board[3] == player[2] and board[6] == player[2] and board[9] == player[2]:
        print("Player 2 wins! " + emojize(":party_popper:"))
        return True
    elif board[1] == player[2] and board[5] == player[2] and board[9] == player[2]:
        print("Player 2 wins! " + emojize(":party_popper:"))
        return True
    elif board[3] == player[2] and board[5] == player[2] and board[7] == player[2]:
        print("Player 2 wins! " + emojize(":party_popper:"))
        return True
    else:
        return False

def run_turn(num):
    global current
    current = num
    pos = input("Choose a square player " + str(current) + " (" + player[int(num)] + "): ")
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