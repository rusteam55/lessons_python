class Complex_num:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'a + b * j'
    def __str__(self):
        return f'комплексное число = {self.a}+{self.b}*j'
    def __add__(self, other):
        if (self.b + other.b ) < 0:
            znak = ''
        else:
            znak = '+'
        return f'Сумма комплексных чисел = ({self.a + other.a} {znak} {self.b + other.b}*j)'

    def __mul__(self, other):
        if (self.b * other.a + (self.a * other.b )) < 0:
            znak = ''
        else:
            znak = '+'
        return f'Произведение комплексных чисел = ({self.a * other.a - (self.b * other.b)} {znak} {self.b * other.a + (self.a * other.b )}*j)'


cn_1 = Complex_num(-4, 2)
cn_2 = Complex_num(3, 5)

print(cn_1)
print(cn_2)
print(cn_1 + cn_2)
print(cn_1 * cn_2)