time = int(input("Введите любое количество секунд...  "))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = (time % 3600) % 60
print(f'{hours // 10}{hours % 10}:{minutes // 10}{minutes % 10}:{seconds // 10}{seconds % 10}')
