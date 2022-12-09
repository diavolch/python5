'''Создайте программу для игры в ""Крестики-нолики"".'''
from random import randint

board = [i for i in range(0,9)]

def draw_board(b):
    print(f'| {board[0]} | {board[1]} | {board[2]} |')
    print('-------------')
    print(f'| {board[3]} | {board[4]} | {board[5]} |')
    print('-------------')
    print(f'| {board[6]} | {board[7]} | {board[8]} |')

draw_board(board)

player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')

flag = randint(0,2)

if flag:
    print(f'Первый ход делает {player1}')
else:
    print(f'Первый ход делает {player2}')

def end_of_the_game(board,count):
    end = True
    if (board[0] == board[4] == board[8] 
        or board[2] == board[4] == board[6]
        or board[1] == board[4] == board[7]
        or board[3] == board[4] == board[5]
        or board[0] == board[1] == board[2]
        or board[3] == board[4] == board[5]
        or board[6] == board[7] == board[8]):
        return end
    elif count == 9:
        return end
    else:
        return False

count = 0
while not end_of_the_game(board,count):
    if flag:
        a = int(input(f'{player1}, введите ячейку, в которую поставите крестик: '))
        board[a] = 'x'
        draw_board(board)
        flag = False
        count += 1
    else:
        a = int(input(f'{player2}, введите ячейку, в которую поставите нолик: '))
        board[a] = '0'
        draw_board(board)
        flag = True
        count += 1

if count < 9:
    if flag:
        print(f"Выиграл {player2}")
    else:
        print(f"Выиграл {player1}")
else:
    print('Ничья!')