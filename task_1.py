# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. 
# Используйте для решения лямбда-функцию.
import random
def generateRandomList():
    list1 = [random.randint(1, 10) for i in range(10)]
    print(list1)
    return list1
listSorted = list(filter(lambda x: int(x) > 5, generateRandomList()))
print(listSorted)
