# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, 
# описывающие возрастающую последовательность. Порядок элементов менять нельзя.

import random
size = 30
numbers = [random.randint(1, 100) for i in range(size)]
print(numbers)
def createRandomSlice():
    slice = []
    indexStart = random.randint(0, size)
    indexFinish = random.randint(indexStart, size)
    for i in range(indexStart, indexFinish):
        slice.append(numbers[i])
    return(slice)

slice = createRandomSlice()
def createGrowingArray():
    numbersNew = []
    a = random.randint(0, len(slice)-1)
    maximum = slice[a]
    for a in range(a,len(slice)-1):
        if slice[a+1] > maximum:
            numbersNew.append(slice[a+1])
            maximum = slice[a+1]      
        a +=1
    return numbersNew
print(f'Случайная возрастающая последовательность списка: {createGrowingArray()}')


