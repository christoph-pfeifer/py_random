import random as r

def function_board():
    if field == 1:
        board_one()
    elif field == 2:
        board_two()
    elif field == 3:
        board_three()
    elif field == 4:
        board_four()
    elif field == 5:
        board_five()
    elif field == 6:
        board_six()
    elif field == 7:
        board_seven()
    elif field == 8:
        board_eight()
    elif field == 9:
        board_nine()
    elif field == 10:
        board_ten()
    elif field == 11:
        board_eleven()
    elif field == 12:
        board_twelve()
    elif field == 13:
        board_thirteen()
    elif field == 14:
        board_fourteen()
    elif field == 15:
        board_fifteen()
    elif field == 16:
        board_sixteen()
    elif field == 17:
        board_seventeen()
    elif field == 18:
        board_eighteen()
    elif field == 19:
        board_nineteen()
    elif field == 20:
        board_twenty()
    elif field == 21:
        board_win()
    elif field > 21:
        board_over()        
    else:
        print('error')

def board_one():
    global field
    field = field +3
    print('you climed a small ladder to field 4', field)
    next_move()

def board_two():
    print('now on field 2', field)
    next_move()

def board_three():
    print('now on field 3', field)
    next_move()

def board_four():
    print('now on field 4', field)
    next_move()

def board_five():
    global field
    field = field -3
    print('you hit a mini-sledge and dropped to field 2', field)
    next_move()

def board_six():
    global field
    field = field +6
    print('you climed a large ladder to field 12', field)
    next_move()

def board_seven():
    print('now on field 7', field)
    next_move()

def board_eight():
    print('now on field 8', field)
    next_move()

def board_nine():
    print('now on field 9', field)
    next_move()

def board_ten():
    global field
    field = field -6
    print('you hit a large sledge and dropped to field 4', field)
    next_move()

def board_eleven():
    print('now on field 11', field)
    next_move()

def board_twelve():
    print('now on field 12', field)
    next_move()

def board_thirteen():
    global field
    field = field +6
    print('you climed a large ladder to field 19', field)
    next_move()

def board_fourteen():
    print('now on field 14', field)
    next_move()

def board_fifteen():
    print('now on field 15', field)
    next_move()

def board_sixteen():
    print('now on field 16', field)
    next_move()

def board_seventeen():
    print('now on field 17', field)
    next_move()

def board_eighteen():
    print('now on field 18', field)
    next_move()

def board_nineteen():
    print('now on field 19', field)
    next_move()

def board_twenty():
    global field
    field = field -8
    print('you hit a very large sledge and dropped to field 12', field)
    next_move()

def board_over():
    global field
    field = field - player
    print('too high, try again', field)
    next_move()

def board_win():
    print('congrats, you win', field)
    start_game()

def next_move():
    answer = input("enter yes to throw the dice again").upper()
    if answer == "YES":
        global field
        global player
        player = r.randint(1, 6)
        field = field + player
        print('you throw a', player)
        function_board()           
    elif answer == "NO":
        print('ok. good bye!')

start = 0

def start_game():
    answer = input("new game! enter yes to throw the dice").upper()
    if answer == "YES":
        global field
        player = r.randint(1, 6)
        field = start + player
        print('you throw a', player)
        function_board()        
    elif answer == "NO":
        print('ok. good bye!')

start_game()

#player_two = r.randint(1, 6) + r.randint(1, 6) # generating random number
#print('player 2 has', player_two)