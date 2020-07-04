class Ceil:
    def __init__(self, num):
        self.num = int(num)
    def __str__(self):
        return f"клетка {self.num * '*'}"
    def __add__(self, other):
        return Ceil(self.num + other.num)
    def __sub__(self, other):
        return Ceil(self.num - other.num if (self.num - other.num) > 0 else print("Разность клеток отрицательна!"))
    def __mul__(self, other):
        return Ceil(int(self.num * other.num))
    def __truediv__(self, other):
        return Ceil(int(self.num) // int(other.num))
    def make_order(self, dig):
        row = ''
        for i in range(int(self.num / dig)):
            row += f"{'*' * dig}\n"
        row += f"{'*' * (self.num % dig)}"
        return row

ceil_1 = Ceil(26)
ceil_2 = Ceil(11)
print(ceil_1)
print(ceil_2)
print(ceil_1 + ceil_2)
print(ceil_1 - ceil_2)
print(ceil_1 * ceil_2)
print(ceil_1 / ceil_2)
print(ceil_2.make_order(3))
print(ceil_1.make_order(10))
