def my_func():
    var_1 = float(input('Введите первое число '))
    var_2 = float(input('Введите второе число '))
    var_3 = float(input('Введите третье число '))
    m = min(var_1, var_2, var_3)
    return var_1 + var_2 + var_3 - m


print(my_func())
