with open("task1.txt", 'r', encoding='utf-8') as count_str:
    print(f'Содержание файла:\n{count_str.read()}')

    count_str.seek(0)
    lines = 0
    for line in count_str:
        lines += 1
    print(f'Количество строк в файле - {lines}')

    count_str.seek(0)
    words = count_str.read()
    words = words.split()
    print(f'Количество слов в файле - {len(words)}')
