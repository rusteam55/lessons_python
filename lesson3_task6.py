sentence = input('Введите несколько слов маленькими латинскими буквами, слова разделяйте пробелом ').split()
new_sentence = []
for n in sentence:
    def int_func():
        lit_list = list(n)
        for i in lit_list:
            if 97 >= ord(i):
                print('Вы ввели некорректное значение')
                return
            if 122 <= ord(i):
                print('Вы ввели некорректное значение')
                return
        word = (''.join(lit_list)).title()
        new_sentence.append(word)


    int_func()

print(' '.join(new_sentence))
