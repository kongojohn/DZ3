# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


list = [float(i) for i in input("введите посследовательность: ").split()]

min_num = list [0]
max_num = 0

for n in list:
    n = n % 1
    if n != 0:
        if n > max_num: max_num = n
        if n < min_num: min_num = n

print (max_num - min_num)
