# Создать массив из 100 целочисленных рандомных чисел, вывести их в консоль
# В целочисленной последовательности есть нулевые элементы. Создать массив из номеров этих элементов.

import random

index = []
num = []
for i in range(100):
    num.append(random.randint(0, 100))
print(num)


for i in range(len(num)):
    if num[i] == 0:
        index.append(i)
print(index)

