def my_func(x, y):
    if x <= 0:
        x = abs(x)
        print('Первое число преобразовано в положительное согласно условию ')
    if y >= 0:
        y = -y
        print('Второе число преобразовано в отрицательное согласно условию')
    y = -y
    x = 1 / x
    count = 1
    while y > 0:
        count = count * x
        y = y - 1
    return count


print(my_func(float(input('Введите положительное число ')), int(input('Введите целое отрицательное число '))))
