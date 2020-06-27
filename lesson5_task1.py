with open("task1.txt", 'w', encoding="utf-8") as task1_obj:
    str = input("Введите данные, которые необходимо записать в файл ")
    while str:
        task1_obj.write(str + '\n')
        str = input("Введите данные, которые необходимо записать в файл ")




