class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []

while True:
    data = input("Введите числа для добавления в список. Для выхода из программы наберите 'stop'. ").lower()
    if data == "stop":
        print(f"Сформирован следующий список: {my_list}")
        break
    else:
        try:
            if data.isnumeric():
                my_list.append(data)
            else: raise MyOwnErr("Введено недопустимое значение")

        except MyOwnErr as ValErr:
            print(ValErr)


