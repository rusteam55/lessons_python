from itertools import count
from math import factorial

def gen():
    for el in range(1, (int(input('Введите число, вплоть до которого будут расчитаны факториалы '))+1)):
        yield factorial(el)

for el in gen():
    print(el)

# проверка в цикле вызова функции:

def gen():
    for el in count(1):
        yield factorial(el)
num = 0
end = int(input('Введите число, вплоть до которого будут расчитаны факториалы '))
for el in gen():
    if num < end:
        print(el)
        num = num + 1
    else:
        break

