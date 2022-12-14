# 1.# Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141
# Ввод: 0.01
#     Вывод: 3.14

#     Ввод: 0.001
#     Вывод: 3.141


# import math
# pinumber = str(math.pi)

# d = input("Введите точность вывода числа pi: ")
# print(len(d))
# # d = d.split('.')
# # print(d)
# # print(len(d[1]))
# x = ''
# y = 0
# for i in pinumber:
#     if y < len(d):
#          x = x + i
#     else:
#         break
#     y +=1
# print(x)
# 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# def justop(n:int):

#     i = 2
#     x = n%i
#     lst = []
#     while n != 1:
#         if n%i==0:
#             n = n/i
#             lst.append(i)
#         else:
#             i+=1
#     return lst


# n = int(input('Введите число N: '))

# print(justop(n))


# 3.Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

# lst = [1, 1, 2, 3, 4, 4, 4, 5, 6, 7, 7, 7, 7]
# newlst = []
# count = 0
# for i in range(len(lst)):
#     for j in range(len(lst)):
#         if lst[i] == lst[j]:
#             count += 1

#     if count == 1:
#         newlst.append(lst[i])
#     count = 0

# print(newlst)

# 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

# import random


# k = int(input('Введите степень: '))


# y = ''

# while k != 0:

#     x = random.randint(0, 100)

#     if x == 0:
#         k -= 1
#         if k == 0 and len(y)<3:
#             print('все элементы уравнения - 0')

#         elif k == 0 and len(y)>3:
#             y = y[:-2]
#             y = y + str('= 0')


#         continue

#     elif k == 1:
#         y = y + str(f'{x}*x + ')

#     else:
#         y = y + str(f'{x}*x**{k} + ')

#     k -= 1
#     if k == 0:
#         x = random.randint(0, 100)
#         y = y + str(f'{x} ')
#         y = y + str('= 0')


# print(y)

# file_path = 'homework.txt'

# with open (file_path,'w') as data_f:
#     data_f.write(y)


# 5.Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).


file_path_a = 'hometa.txt'
file_path_b = 'homeb.txt'

with open(file_path_a, 'r') as data_a:
    lst = data_a.read()

with open(file_path_b, 'r') as data_b:
    lstb = data_b.read()


lst = lst[:-4]
lstb = lstb[:-4]
summlist = []
summlist_b = []
newlist = []


lst = lst.split(' + ')
lstb = lstb.split(' + ')




print(lst)
print(lstb)

for i in range(len(lst)):
    summlist.append((lst[i].split('*x')))
    summlist_b.append((lstb[i].split('*x')))

print(summlist)
print(summlist_b)

for i in range(len(summlist)-2):
    for j in range(len(summlist_b)-2):
        

        if summlist[i][-1][-1] == summlist_b[j][-1][-1]:
            newlist.append(int(summlist[i][0]) + int(summlist_b[j][0]))

newlist.append(int(summlist[-2][0]) + int(summlist_b[-2][0]))
newlist.append(int(summlist[-1][0]) + int(summlist_b[-1][0] ))

print(newlist)

finalsumm = ''

for i in range(len(newlist)):
    if i == len(newlist)-2:
        finalsumm = finalsumm + str(newlist[i])+(f'*x + ')
        continue
    if i == len(newlist)-1:
        finalsumm = finalsumm + str(newlist[i])+ (' = 0')
        continue
    finalsumm = finalsumm + str(newlist[i])+(f'*x**{len(newlist)-1-i} + ')
    
print(finalsumm)

with open(file_path_a, 'r') as data_a:
    lst = data_a.read()

with open(file_path_b, 'r') as data_b:
    lstb = data_b.read()


file_path_summ = 'homesumm.txt'
with open(file_path_summ, 'w') as data_c:
    data_c.write(lst + '\n')
    data_c.write(lstb + '\n')
    data_c.write(finalsumm)