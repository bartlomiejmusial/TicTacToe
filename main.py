# Tic Tac Toe
from random import choice

table = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def display_table():
    """
    This function displays a table after each move
    """
    board = f"""
         |     |    
      {table[7]}  |  {table[8]}  |  {table[9]}
         |     |
    -----------------
         |     |    
      {table[4]}  |  {table[5]}  |  {table[6]}
         |     |
    -----------------
         |     |    
      {table[1]}  |  {table[2]}  |  {table[3]}
         |     |
    """
    print(board)


def who_starts():
    """
    In this function players choose which character (x or y) starts
    :return list of players characters [player1, player2]
    """
    player1 = ''
    while player1 not in ['x', 'o', 'r']:
        player1 = input("Choose who starts. Type 'o' or 'x' or 'r' if you want a random choice: ").lower()
        if player1 == 'r':
            return choice([['x', 'o'], ['o', 'x']])
        if player1 == 'o':
            return ['x', 'o']
        elif player1 == 'x':
            return ['o', 'x']
        else:
            print("The character which you entered is not a x or o. Try again!\n")


def check_full():
    """
    This function checks if the table is full
    Returns True if it is, and False if not
    """
    if table[1] in ['x', 'o'] and table[2] in ['x', 'o'] and table[3] in ['x', 'o'] and table[4] in ['x', 'o'] \
            and table[5] in ['x', 'o'] and table[6] in ['x', 'o'] and table[7] in ['x', 'o'] \
            and table[8] in ['x', 'o'] and table[9] in ['x', 'o']:
        print("Table is full!\nGAME OVER!")
        return False
    else:
        return True


def is_win(player_char):
    """
    A function which checks all the possibilities of winning
    :param player_char: player character
    :return: boolean value of True - win and False - there is no win
    """
    if table[1] == table[2] == table[3] == player_char:
        print(f"{player_char} wins!")
        return True
    if table[4] == table[5] == table[6] == player_char:
        print(f"{player_char} wins!")
        return True
    if table[7] == table[8] == table[9] == player_char:
        print(f"{player_char} wins!")
        return True
    if table[1] == table[4] == table[7] == player_char:
        print(f"{player_char} wins!")
        return True
    if table[2] == table[5] == table[8] == player_char:
        print(f"{player_char} wins!")
        return True
    if table[3] == table[6] == table[9] == player_char:
        print(f"{player_char} wins!")
        return True
    if table[1] == table[5] == table[9] == player_char:
        print(f"{player_char} wins!")
        return True
    if table[7] == table[5] == table[3] == player_char:
        print(f"{player_char} wins!")
        return True


def play_game():
    """
    Main function of the game
    """
    global table
    print('\n' * 100)
    print("Welcome to The Tic Tac Toe Game!")
    table = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    turn = 0
    game = True
    players = who_starts()
    display_table()
    while game:
        if turn % 2 == 0:
            player = players[0]
        else:
            player = players[1]
        position = "WRONG"
        while position.isdigit() is False or int(position) not in list(range(1, 10))\
                or table[int(position)] in ['x', 'o']:
            position = (input(f"Player {player}, choose the position (1-9): "))
            if position.isdigit() is False:
                print("It's not a digit!")
                continue
            if int(position) not in list(range(1, 10)):
                print("It's not a digit in range (1-9)!\nTry again")
            if table[int(position)] in ['x', 'o']:
                print(f"This field is already taken by {table[int(position)]}!\n")

        table[int(position)] = player

        print('\n' * 100)
        display_table()
        game = check_full()
        if is_win(player) or game is False:
            again = ''
            while again not in ['yes', 'no']:
                again = input("\nPlay again? Type yes or no: ").lower()
                if again == 'no':
                    print("Exiting...")
                    return
                elif again == 'yes':
                    play_game()
                else:
                    print("Invalid value!\n")
        turn += 1


play_game()
