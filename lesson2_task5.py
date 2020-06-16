my_list = [7, 5, 3, 3, 2]
new_list = my_list.copy()
enter_el = input('Введите любое натуральное число ')

for i in my_list:
    if i < int(enter_el):
        ind = my_list.index(i)
        break
    elif my_list.index(i) != len(my_list) - 1:
        continue
    else:
        ind = len(my_list)

new_list.insert(ind, enter_el)
print(new_list)
