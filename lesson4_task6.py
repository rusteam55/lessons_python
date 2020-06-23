from itertools import count, cycle, islice

my_list = []
for el in islice(count(), int(input('Введите целое начальное число генерируемой последовательности ')),
                 (int(input('Введите целое конечное число генерируемой последовательности ')) + 1)):
    print(el)
    my_list.append(el)
for el in islice(cycle(my_list), int(input('Введите сколько раз необходимо повторить элементы последовательности  '))):
    print(el)
