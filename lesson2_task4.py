words = input('Введите строку из нескольких слов, разделённых пробелами ')
words_list = words.split()
print(words_list)

for i, v in enumerate(words_list, 1):
    print(i, v[0:10])
