subj_list = []
clock_list = []
with open("text_6.txt", 'r', encoding='utf-8') as subjects:
    for line in subjects:
        i = line.split()
        subj_list.append(i[0])
        num = i[1].split('(') + i[2].split('(') + i[3].split('(')
        clock_list.append(sum([int(s) for s in num if s.isdigit()]))
my_dict = dict(zip(subj_list, clock_list))

print(my_dict)
