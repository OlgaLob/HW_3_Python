# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй 
# и предпоследний и т.д.
#     *Пример:*
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]
import random
from random import randint
rand_list=[]
rand_list_new = []
n = random.randint(1, 10)
for i in range(n):
    rand_list.append(random.randint(1, 10))
print(rand_list)
for i in range(len(rand_list)):
    while i < len(rand_list)/2 and n > len(rand_list)/2:
        n = n - 1
        a = rand_list[i] * rand_list[n]
        rand_list_new.append(a)
        i += 1
print(rand_list_new)


