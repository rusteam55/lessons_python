my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[ind] for ind in range(1, len(my_list)) if my_list[ind] > my_list[ind - 1]]
print(my_list)
print(new_list)
