import random

try:
    with open("task5.txt", 'w', encoding='utf-8') as calc_obj:
        print('Для генерации числа нажмите клавишу Enter. Для завершения генерации нажмите клавишу q ')
        quit = None
        while quit != 'q':
            num = str(random.randint(0, 100))
            print(num)
            calc_obj.writelines(num + ' ')
            quit = input()
    with open("task5.txt", 'r', encoding='utf-8') as calc_obj:
        for line in calc_obj:
            number = line.split()
            print(f'Сумма чисел составляет {sum(map(float, number))}')

except IOError:
    print("Произошла ошибка ввода-вывода")
