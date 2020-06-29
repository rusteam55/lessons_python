class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


p_1 = Position("Ivan", "Petrov", "manager", 150000, 50000)
print(p_1.get_full_name())
print(p_1.get_total_income())

p_2 = Position("Petr", "Ivanov", "assistant", 90000, 40000)
print(p_2.get_full_name())
print(p_2.get_total_income())
