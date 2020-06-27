from translate import Translator

translator = Translator(from_lang="english", to_lang="russian")
rus_list = []
with open('text_4.txt', 'r+', encoding='utf-8') as origin_obj:
    for line in origin_obj:
        i = line.split()
        rus_list.append(translator.translate(i[0]) + ' ' + i[1] + ' ' + i[2])
print(rus_list)

with open('text_4_rus.txt', 'w', encoding='utf-8') as new_obj:
    for i in rus_list:
        new_obj.writelines(i + '\n')
