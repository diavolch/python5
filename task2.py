'''Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая 
ход друг после друга. Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?'''

from random import randint

player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')

flag = randint(0,2)

if flag:
    print(f'Первый ход делает {player1}')
else:
    print(f'Первый ход делает {player2}')

count1 = 0
count2 = 0
candies = 2021

while candies > 28:
    if flag: 
        k = int(input(f'{player1}, введите количество конфет, которое возьмете от 1 до 28: '))
        count1 += k
        candies -= k
        flag = False
        print(f'Ходил {player1}, взял {k} кофет,теперь у него {count1} кофет, на столе осталось {candies}.')
    else: 
        k = int(input(f'{player2}, введите количество конфет, которое возьмете от 1 до 28: '))
        count2 += k
        candies -= k
        flag = True
        print(f'Ходил {player2}, взял {k} кофет,теперь у него {count2} кофет, на столе осталось {candies}.')


if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")


# a) Добавьте игру против бота
# то же самое, только для второго игрока в цикл записывать:
#        k = randint(0,28)
