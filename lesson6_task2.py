class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        print(f'Длина дороги {length} м')
        print(f'Ширина дороги {width} м')

    def mass(self):
        m = self._length * self._width * 125 / 1000
        print(f'Масса асфальта составляет {m} т.')


m1 = Road(5000, 20)
m1.mass()
m2 = Road(3000, 15)
m2.mass()
m3 = Road(10000, 10)
m3.mass()
