my_list = list(input('Введите список из любых значений  '))
length = len(my_list) % 2
checked = length != 0
end = (len(my_list), len(my_list)-1)[checked]
my_list[:end:2], my_list[1:end:2] = my_list[1:end:2], my_list[:end:2]

print(my_list)
