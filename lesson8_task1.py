class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def transform_dig(cls, day_month_year):
        dig_list = []
        for i in day_month_year.split('-'):
            if i.isdigit(): dig_list.append(int(i))
            else: raise SystemExit

        date_1_1 = cls(dig_list[0], dig_list[1], dig_list[2])
        Date.validation(dig_list[0], dig_list[1], dig_list[2])
        return date_1_1

    @staticmethod
    def validation(day, month, year):
        long_month = [1, 3, 5, 7, 8, 10, 12]
        short_month = [4, 6, 9, 11]
        if month in long_month:
            if 1 <= day <= 31:
                if 1900 <= year <= 2020:
                    print("Это великолепная дата!")
                else:
                    print("Недопустимый год")
            else:
                print("Такой даты не существует")
        elif month in short_month:
            if 1 <= day <= 30:
                if 1900 <= year <= 2020:
                    print(f"{day} - {month} - {year}. Это великолепная дата!")
                    #print("Это великолепная дата!")
                else:
                    print("Недопустимый год")
            else:
                print("Такой даты не существует")
        elif month == 2:
            if 1 <= day <= 28:
                if 1900 <= year <= 2020:
                    print(f"{day} - {month} - {year}. Это великолепная дата!")
                    #print("Это великолепная дата!")
                else:
                    print("Недопустимый год")
            else:
                print("Такой даты не существует")
        else:
            print("Неверное значение месяца")
        #print (f"{day} - {month} - {year}")
        #return day and month and year

date_1 = Date.transform_dig(f'{input("Введите день месяца  ")}-{input("Введите номер месяца ")}-{input("Введите год ")}')

