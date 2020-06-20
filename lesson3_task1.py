def divide(var_1, var_2):
    try:
        print(round(var_1 / var_2, 2))
    except ZeroDivisionError:
        return print('На 0 делить нельзя!')


divide(float(input('Введите число (делимое) ')), float(input('Введите число (делитель) ')))
