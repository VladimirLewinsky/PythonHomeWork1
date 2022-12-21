#                                 1.Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# tekst = 'Я люблю Джавуабв абви Питон абвабв абв'


# tekst = tekst.split(' ')
# print(tekst)
# newtekst = [i for i in tekst if 'абв' not in i]

# print(' '.join(newtekst))


#                               2.Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
#  За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""
# Сколько конфет нужно взять первому игроку  Ответ:1992 конфеты

# import random


# def gamemodefrined(lottery, candy, player1_basket, player2_basket):
#     while candy > 0:

#         if lottery == 0:
#             print("ходит player1")
#             print(f'у вашего оппонента {player2_basket}  конфет')
#             print(f'на столе осталось {candy}')

#             try:
#                 player1_move = int(input("Сколько конфет хотите взять "))
#                 if 0 >= player1_move or player1_move > 28:
#                     raise ValueError()
#             except ValueError:
#                 print("За ход можно взять от 1 до 28, возьми снова")
#                 continue

#             player1_basket = player1_basket + player1_move + player2_basket
#             candy = candy - player1_move
#             player2_basket = 0
#             if candy <=0:
#                 print('победил player 1')
#                 continue

#             print(f'на столе осталось {candy}')
#             lottery += 1

#         if lottery == 1:
#             print("ходит player2")
#             print(f'у вашего оппонента {player1_basket}  конфет')
#             print(f'на столе осталось {candy}')
#             try:
#                 player2_move = int(input("Сколько конфет хотите взять "))
#                 if 0 >= player2_move or player2_move > 28:
#                     raise ValueError()
#             except ValueError:
#                 print("За ход можно взять от 1 до 28, возьми снова")
#                 continue

#             player2_basket = player2_basket + player2_move + player1_basket
#             candy = candy - player2_move
#             player1_basket = 0
#             if candy <=0:
#                 print('победил player 2')
#                 continue
#             print(f'на столе осталось {candy}')
#             lottery -= 1


# def gamemodebot(lottery, candy, player1_basket, player2_basket):
#     while candy > 0:

#         if lottery == 0:
#             print("ходит player1")
#             print(f'у вашего оппонента {player2_basket}  конфет')
#             print(f'на столе осталось {candy}')

#             try:
#                 player1_move = int(input("Сколько конфет хотите взять "))
#                 if 0 >= player1_move or player1_move > 28:
#                     raise ValueError()
#             except ValueError:
#                 print("За ход можно взять от 1 до 28, возьми снова")
#                 continue

#             player1_basket = player1_basket + player1_move + player2_basket
#             candy = candy - player1_move
#             player2_basket = 0
#             if candy <= 0:
#                 print('победил player 1')
#                 continue

#             print(f'на столе осталось {candy}')
#             lottery += 1

#         if lottery == 1:
#             print("ходит bot")
#             print(f'у вашего оппонента {player1_basket}  конфет')
#             if candy > 29 and candy < 100 and candy%28 != 0:
#                 x = candy % 28
#                 player2_move = x -1
#                 print(f'Бот взял: {player2_move}')

#             elif candy <= 28:
#                 player2_move = candy
#                 print(f'Бот взял: {player2_move}')
#             else:
#                 player2_move = random.randint(1, 28)
#                 print(f'Бот взял: {player2_move}')
#             player2_basket = player2_basket + player2_move + player1_basket
#             candy = candy - player2_move
#             player1_basket = 0
#             if candy <=0:
#                 print('победил bot')
#                 continue
#             print(f'на столе осталось {candy}')
#             lottery -= 1


# candy = 2021
# lottery = random.randint(0, 1)
# player1_basket = 0
# player2_basket = 0

# mode = int(input(
#     'Если хотите играть с ботом введите 0, если хотите играть с другом введите 1: '))
# if mode == 1:

#     gamemodefrined(lottery, candy, 0, 0)
# if mode == 0:
#     gamemodebot(lottery, candy, 0, 0)


#                                 3.Создайте программу для игры в ""Крестики-нолики"".

# print(" Игра крестики Нолики")
# print("\n")
# print(f"\t {0} | {1} | {2}")
# print("\t __|___|___")
# print(f"\t {4} | {5} | {6}")
# print("\t __|___|___")
# print(f"\t {7} | {8} | {9}")
# print("\n")


# try:
#     chooseside = int(input("Выберите какими символами будете играть 1 - X , 2 - O: "))
#     if 1 > chooseside or chooseside > 2:
#         raise ValueError()
# except ValueError:
#     print('Введите 1 или 2, попробуйте снова')


# weald = {i: i for i in range(9)}
# x = 0
# count = 0
# while x != 1:
#     pl1_move = int(input(" ваш ход: "))
#     weald[pl1_move] = "X"
#     print("\n")
#     print(f"\t {weald[0]} | {weald[1]} | {weald[2]}")
#     print("\t __|___|___")
#     print(f"\t {weald[3]} | {weald[4]} | {weald[5]}")
#     print("\t __|___|___")
#     print(f"\t {weald[6]} | {weald[7]} | {weald[8]}")
#     print("\n")
#     count+=1
#     if (weald[0] == weald[1] == weald[2]) or (weald[3] == weald[4] == weald[5]) or (weald[6] == weald[7] == weald == [8])\
#             or (weald[0] == weald[3] == weald[6]) or (weald[0] == weald[3] == weald[6]) or (weald[2] == weald[5] == weald == [8])\
#             or (weald[0] == weald[4] == weald[8]) or (weald[2] == weald[4] == weald[6]):

#         print("Победил X")
#         break
#     if count == 9:
#         print("Ничья")
#         break
        

#     pl2_move = int(input(" ваш ход: "))
#     weald[pl2_move] = "O"
#     print("\n")
#     print(f"\t {weald[0]} | {weald[1]} | {weald[2]}")
#     print("\t __|___|___")
#     print(f"\t {weald[3]} | {weald[4]} | {weald[5]}")
#     print("\t __|___|___")
#     print(f"\t {weald[6]} | {weald[7]} | {weald[8]}")
#     print("\n")
#     count+=1
    

#     if (weald[0] == weald[1] == weald[2]) or (weald[3] == weald[4] == weald[5]) or (weald[6] == weald[7] == weald == [8])\
#     or (weald[0] == weald[3] == weald[6]) or (weald[0] == weald[3] == weald[6]) or (weald[2] == weald[5] == weald == [8])\
#     or (weald[0] == weald[4] == weald[8]) or (weald[2] == weald[4] == weald[6]):

#         print("Победил O")
#         break
#     if count == 9:
#         print("Ничья")
#         break


#                  4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


# teststr = 'qqqqqqqqweeeeeeeeebbbrrrsqeeee'

# lst = ''
# i = 0
# while i < len(teststr):
#     count = 1
#     while i +1 <len(teststr) and teststr[i]== teststr[i+1]:
#         count+=1
#         i+=1


#     lst= lst + (str(count) + teststr[i])
#     i+=1

# print(lst)
# newstr = ''
# for i in range(0,len(lst),2):
    
#         newstr = newstr + (int(lst[i])*lst[i+1])

# print(newstr)