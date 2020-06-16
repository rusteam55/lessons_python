my_goods = int(input('Введите сколько позиций Вы планируете ввести '))
my_list = []
for i in range(my_goods):
    dict_good = {}
    dict_good['Наименование'] = input('Введите наименование товара ')
    dict_good['Цена'] = input('Введите цену товара, в руб. ')
    dict_good['Количество единиц'] = input('Введите количество единиц ')
    dict_good['Единицы'] = str('шт')

    tup_good = (i + 1, dict_good)

    my_list.append(tup_good)

for el in my_list:
    print(el)

name_list = []
price_list = []
count_list = []
el_list = []
for i in range(my_goods):
    val_name = my_list[i][1].get('Наименование')
    val_price = my_list[i][1].get('Цена')
    val_count = my_list[i][1].get('Количество единиц')
    val_el = my_list[i][1].get('Единицы')
    name_list.append(val_name)
    price_list.append(val_price)
    count_list.append(val_count)
    el_list.append(val_el)

dict_analytic = {}
dict_analytic['Наименование'] = name_list
dict_analytic['Цена'] = price_list
dict_analytic['Количество единиц'] = count_list
dict_analytic['Единицы'] = list(set(el_list))

for items in dict_analytic.items():
    print(items)
