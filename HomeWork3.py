# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12


# def summlist(lst: list):
#     summ = 0
#     for i in range(len(lst)):

#         if i%2 == 0:
#             i
#         else:
#             summ+= lst[i]
#     return summ


# print(summlist([2, 3, 5, 9, 3]))


# 2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# def oplist(lst: list):
#     newlist =[]


#     for i in range(int((len(lst))/2+0.5)):
#         newlist.append(lst[i]*lst[-1-i])

#     return newlist

# print(oplist([2, 3, 4, 5, 6]))


# 3.Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19


# lst = [1.1, 1.2, 3.1, 10.01 ]
# newlst = []

# for i in range(len(lst)):
#     x = round(lst[i] % 1, 3)
#     newlst.append(x)


# maximum = newlst[0]
# minimum = newlst[0]

# for i in range(len(newlst)):
#     if maximum < newlst[i]:
#         maximum = newlst[i]
#     if newlst[i] < minimum:
#         minimum = newlst[i]

# print(newlst)
# print('Максимальное число ',maximum)
# print('Минимальное число ',minimum)
# print('разница ', maximum - minimum)


# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# x = int(input('Введите число: '))
# y =''
# while x != 0:
#     y = str(x %2) +2
#     x = x //2


# print(y)


# 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример: Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


k = int(input('введите спсиок чисел  фибоначи: '))


y = -k
lst = []
lst2 = []

for i in range(k+1):

    if i == 0:
        lst.append(i)
    if i == 1 or i == 2:
        lst.append(1)

    if i > 2:
        lst.append(lst[i-1]+lst[i-2])


while y <= k:
    if y < 0:
        if y % 2 == 0:
            lst2.append(lst[-y] * -1)
        else:
            lst2.append(lst[-y])

    else:
        lst2.append(lst[y])
    y += 1

print(lst)
print(lst2)
