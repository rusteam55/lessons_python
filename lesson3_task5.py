final_sum = 0
fin = False
while fin == False:
    my_tuple = input('Введите числа через пробел. Для завершения расчета введите клавишу f ')
    my_list = my_tuple.split()
    new_list = []

    for i in my_list:
        if i.isnumeric():
            new_list.append(int(i))
        if i == 'f' or i == 'F':
            fin = True
            break
    print(f'Вы ввели следующие числа {new_list}')
    my_sum = sum(new_list)
    print(f'Сумма введенных чисел составляет {my_sum}')
    final_sum = final_sum + my_sum
    print(f'Общая сумма всех введенных чисел составляет {final_sum}')
