number = int(input('Введите любое целое положительное число: '))

max = 0
while number > 0:
    if number % 10 > max:
        max = number % 10

    number = number // 10

print(max)
