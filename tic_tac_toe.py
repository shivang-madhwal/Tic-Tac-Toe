import random

board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

def print_board():
    print("\n   0  1  2")
    row_no=0
    for row in board:
        print(row_no, row)
        row_no+=1
    print("\n")

def is_empty( row, col):
    if board[row][col]==0:
        return True
    else:
        return False

def turn( player_no):
    valid=False
    
    while valid == False:
        row_no=int (input("row no: "))
        col_no=int (input("column no :"))
        if 0 <= row_no and row_no < 3 and 0 <= col_no and col_no < 3:
            if is_empty( row_no, col_no):
                valid=True
                board[row_no][col_no]=player_no
            else:
                print("Space Occupied\nTry again")
        else:
            print("\nWrong Input \nValid Input values [0,1,2]")
        
def m_turn(machine_no):
    valid=False

    while valid == False:
        row_no=int ( random.choice([0,1,2]) )
        col_no=int ( random.choice([0,1,2]))
        if 0 <= row_no and row_no < 3 and 0 <= col_no and col_no < 3:
            if is_empty( row_no, col_no):
                valid=True
                board[row_no][col_no]=machine_no

def is_winner(player_no):
    win=False

    for row in range(0,3):
      col1=board[row][0]
      col2=board[row][1]
      col3=board[row][2]
    if col1 == col2 == col3 == player_no:
        win = True
        return win

    for row in range(0,3):
      row1=board[0][row]
      row2=board[1][row]
      row3=board[2][row]
    if row1 == row2 == row3 == player_no:
        win = True
        return win

    d1=board[0][0]
    d2=board[1][1]
    d3=board[2][2]
    if d1 == d2 == d3 == player_no:
        win = True
        return win

    d1=board[0][2]
    d2=board[1][1]
    d3=board[2][0]
    if d1 == d2 == d3 == player_no:
        win = True
        return win


print("Welcome to Tic Tac Toe")
repeat = 'y'
while repeat == 'y' or repeat == 'Y':
    board = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    print_board()
    x=8
    m_choice=int (-1)
    valid = False
    while valid == False:
        choice =int (input("Choose what you want 1 or 2\n"))
        if choice == 1 or choice == 2:
            valid = True
        else:
            print("Invalid Input")

    if choice == 1:
        m_choice = 2    
    else:
        m_choice = 1

    print("your turn first")

    while(x):
        turn(choice)
        print_board()
        if x < 5:
            if is_winner(choice) or is_winner(m_choice):
                break
        x=x-1
        m_turn(m_choice)
        print_board()
        if x < 5:
            if is_winner(choice) or is_winner(m_choice):
                break
    
        x=x-1

    result=is_winner(choice)
    if result == True:
        print("You win!!!!!!")
    result = is_winner(m_choice)
    if result == True:
        print("You lost")
    if result == False:
        print("It was a draw")

    repeat = input("Want to play again? (y/n)")

