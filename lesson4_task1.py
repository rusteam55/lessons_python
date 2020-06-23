from sys import argv

script_name, first_param, second_param, third_param = argv

print("Выработка, в часах: ", first_param)
print("Ставка, руб./час: ", second_param)
print("Премия, руб.: ", third_param)


def salary_culc():
    try:
        a = float(first_param)
        b = float(second_param)
        c = float(third_param)
        if a > 0 and b > 0:
            print(f'Расчет заработной платы: {a * b + c} руб.')
        else:
            print('Выработка и ставка не могут иметь отрицательное значение')
    except TypeError:
        return print('Введите числовые, а не текстовые параметры')
    except ValueError:
        return print('Введите числовые, а не текстовые параметры')
    except SyntaxError:
        return print('Недопустимое значение')


salary_culc()
