# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего 
# совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.

import random

numbers = [random.randint(1, 10) for i in range(10)]
print(sorted(numbers))
dct = {}
for i in numbers:
    if i in dct:
        dct[i] +=1
    else:
        dct[i] = 1
count = 0

for item in dct:
    if dct[item] > 1:
        count += dct[item]
print(f'Количество повторяющихся элементов: {count}')
