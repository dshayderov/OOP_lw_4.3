#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать базовый класс Car (машина), характеризуемый торговой маркой (строка), числом
цилиндров, мощностью. Определить методы переназначения и изме нения мощности.
Создать производный класс Lorry (грузовик), характеризуе мый также грузоподъемностью
кузова. Определить функции переназначения марки и изменения грузоподъемности.
"""


class Car:

    def __init__(self, mark, cylinders, power):
        self.mark = str(mark)
        self.cylinders = cylinders
        self.power = power

    # Изменение мощности
    def change_power(self, new_power):
        self.power = new_power

    def __repr__(self):
        return f"Марка: {self.mark}, число цилиндров: {self.cylinders}, мощность: {self.power} л.с."


class Larry(Car):

    def __init__(self, mark, cylinders, power, load):
        super().__init__(mark, cylinders, power)
        self.load = load

    # Переназначение марки
    def change_mark(self, new_mark):
        self.mark = str(new_mark)

    # Изменение грузоподъемности
    def change_load(self, new_load):
        self.load = new_load

    def __repr__(self):
        return f"Марка: {self.mark}, число цилиндров: {self.cylinders}, мощность: {self.power} л.с., грузоподъемность: {self.load} кг"


if __name__ == '__main__':
    # Объект класса "Машина"
    car_1 = Car('Toyota Camry', 6, 150)
    print(car_1)
    # Изменение мощности
    car_1.change_power(181)
    print(car_1)

    # Объект класса "Грузовик"
    larry_1 = Larry('Ford F-MAX', 6, 260, 32000)
    print(larry_1)
    # Изменение марки, мощности и грузоподъемности
    larry_1.change_mark('Ford Cargo')
    larry_1.change_power(300)
    larry_1.change_load(20990)
    print(larry_1)