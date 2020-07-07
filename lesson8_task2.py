class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt

numerator = input("Введите числитель ")
denominator = input("Введите знаменатель ")
try:
    numerator = float(numerator)
    denominator = float(denominator)
    if denominator == 0:
        raise MyOwnErr("На 0 делить нельзя!")
except ValueError:
    print("Error!")
except MyOwnErr as DivErr:
    print(DivErr)
else:
    print("%.4f" % (numerator / denominator))
finally:
    print("The end!")