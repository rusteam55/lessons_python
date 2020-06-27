with open("text_3.txt", 'r', encoding='utf-8') as salary:
    roster = []
    aver_sal = []
    for line in salary:
        i = line.split()
        if float(i[1]) < 20000:
            roster.append(i[0])
        aver_sal.append(i[1])
    print(f'Зарплата ниже 20000 руб. у следующих сотрудников: {roster}')
    average = sum(map(float, aver_sal)) / float(len(aver_sal))
    print(f'Средняя зарплата составляет {average} руб.')
