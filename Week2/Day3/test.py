def set_board():    
    positions = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    return positions

def display_board(pos = None):
    print(f"      1 * 2 * 3 ")
    print("******************")
    print(f" A *  {pos[0]} | {pos[1]} | {pos[2]}  *")
    print("**** === === === *")
    print(f" B *  {pos[3]} | {pos[4]} | {pos[5]}  *")
    print("**** === === === *")
    print(f" C *  {pos[6]} | {pos[7]} | {pos[8]}  *")
    print("******************")

def player_input(player):
    move = (input(f"{player}'s turn, enter your move (A1-C3): ")).upper()
    return move

def check_win(board, player):
    win_condition = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for win in win_condition:
        # if board[win[0]] == board[win[1]] == board[win[2]] == player:
        #     return True
        # else board[win]
        return all(board[inwin] == player for inwin in win)

def check_tie(board):
    # for move in board:
    #     if all(move in ["X", "O"]):
    #         return True 
    # for move in board:
    #     if move not in ["X", "O"]:
    #         return False
    # return TrueSSs
    return all(move in ["X", "O"] for move in board)

def play():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    valid_moves = set_board()
    player = "X"
    on = True

    while on:
        display_board(board)
        move = player_input(player)

        if move in valid_moves:
            board[valid_moves.index(move)] = player
            valid_moves[valid_moves.index(move)] = player 

            if check_win(valid_moves, player):
                display_board(board)
                print(f"{player} wins")
                on = False
            elif check_tie(valid_moves):
                display_board(board)
                print("Tie")
                on = False
            else:
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'
        else :
            print("Enter a valid move")

play()
