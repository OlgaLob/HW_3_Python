# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
#     *Пример:*
#     - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19
import random

rand_list=[]
n = random.randint(1, 10)
for i in range(n):
    rand_list.append(round((random.uniform(1, 10)), 2))
print(rand_list)
rand_list_new = [round(i%1,2) for i in rand_list if i%1 != 0]
print(round((max(rand_list_new) - min(rand_list_new)), 2))