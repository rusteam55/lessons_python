from abc import ABC, abstractmethod
class Clothes(ABC):
    @abstractmethod
    def cloth_calc(self):
        pass

class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    # создаем свойство размер
    @property
    def size(self):
        return self.__size

    # создаем сеттер для создания свойств размера
    @size.setter
    def size(self, size):
        if size < 46:
            self.__size = 46
        elif size > 64:
            self.__size = 64
        else:
            self.__size = size

    # расчет расхода ткани
    def cloth_calc(self):
        cloth_calcul = float('{:.2f}'.format(self.size / 6.5 + 0.5))
        return cloth_calcul

    # возвращаем выбранный размер и расход ткани
    def get_coat_size(self):
        return f"Для пальто {str(self.size)} размера требуется {self.cloth_calc()} метров ткани "

class Suit(Clothes):
    def __init__(self, size):
        self.size = size

    # создаем свойство размер
    @property
    def size(self):
        return self.__size

    # создаем сеттер для создания свойств размера
    @size.setter
    def size(self, size):
        if size < 1.5:
            self.__size = 1.5
        elif size > 2:
            self.__size = 2
        else:
            self.__size = size

    # расчет расхода ткани
    def cloth_calc(self):
        cloth_calcul = float('{:.2f}'.format(self.size *2 + 0.3))
        return cloth_calcul

    # возвращаем выбранный размер и расход ткани
    def get_coat_size(self):
        return f"Для костюма на рост {str(self.size)} м. требуется {self.cloth_calc()} метров ткани "

coat = Coat(70)
suit = Suit(1.8)

print(coat.get_coat_size())
print(suit.get_coat_size())


