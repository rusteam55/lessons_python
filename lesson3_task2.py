def personal(name, surname, born, city, email, phone):
    print(f'{name}, {surname}, {born}, {city}, {email}, {phone}')


personal(name=input('Введите имя '), surname=input('Введите фамилию '), born=input('Введите год рождения '),
         city=input('Введите город проживания '), email=input('Введите email '), phone=input('Введите номер телефона '))
