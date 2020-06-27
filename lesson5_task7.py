import json

firm_profit = {}
profit_list = []
aver_profit = {}
with open("text_7.txt", 'r', encoding='utf-8') as pl_obj:
    for line in pl_obj:
        name, form, earnings, costs = line.split()
        pl = int(earnings) - int(costs)
        firm_profit[name] = pl
        if pl > 0:
            profit_list.append(pl)
    aver_profit["average profit"] = sum(profit_list) / len(profit_list)
my_list = [firm_profit, aver_profit]
print(my_list)

with open("text_77.json", 'w', encoding='utf-8') as j_obj:
    json.dump(my_list, j_obj, indent=4, ensure_ascii=False)
