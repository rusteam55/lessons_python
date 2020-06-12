first_distance = int(input('В первый день спортсмен пробежал ... км. Введите значение '))
last_distance = int(input('Цель спортсмена ... км. Введите значение '))
day = 0
while True:
    day = day + 1
    if first_distance >= last_distance:
        break
    first_distance = first_distance + (first_distance / 10)

print(f'Ответ: на {day}-й день спортсмен достиг результата - не менее {last_distance} км')
