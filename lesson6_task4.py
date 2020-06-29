import random


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Автомобиль {self.name}, цвет {self.color}.')

    def go(self):
        print(f'Автомобиль {self.name} тронулся с места')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self):
        direction = ["направо", "налево"]
        print(f'Автомобиль {self.name} повернул {random.choice(direction)}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} составляет {self.speed} км/ч')


class townCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Автомобиль {self.name} превышает скорость")


class sportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class workCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Автомобиль {self.name} превышает скорость")


class policeCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

        if self.is_police:
            print(f'Автомобиль {self.name} - это полицейская машина')


car_1 = policeCar(90, "blue", "UAZ", True)
car_2 = workCar(60, "white", "KRAZ", False)
car_3 = townCar(70, "red", "Nissan", False)
car_4 = sportCar(150, "yellow", "Lamborghini", False)
car_1.go()
car_1.turn()
car_1.show_speed()
car_2.go()
car_2.show_speed()
car_2.turn()
car_2.stop()
car_3.go()
car_3.turn()
car_3.show_speed()
car_4.go()
car_4.show_speed()
car_4.turn()
car_4.stop()
