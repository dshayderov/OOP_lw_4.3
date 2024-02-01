#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать абстрактный класс Currency (валюта) для работы с денежными суммами.
Определить виртуальные функции перевода в рубли и вывода на экран.
Реализовать производные классы Dollar (доллар) и Euro (евро) со своими функциями перевода и вывода на экран.
"""

from abc import ABC, abstractmethod


class Currency(ABC):

    # Функция перевода в рубли
    @abstractmethod
    def to_rubles(self, value):
        pass

    # Функция вывода на экран
    @abstractmethod
    def display(self):
        pass


class Dollar(Currency):

    def __init__(self, denomination):
        self.denomination = float(denomination)

    def to_rubles(self, value):
        print(f"{value} \u0024 = {value * self.denomination} \u20bd")

    def display(self):
        print(f"Курс доллара: \u0024 1 = {self.denomination} \u20bd ")


class Euro(Currency):

    def __init__(self, denomination):
        self.denomination = float(denomination)

    def to_rubles(self, value):
        print(f"{value} \u20ac = {value * self.denomination} \u20bd")

    def display(self):
        print(f"Курс евро: \u20ac 1 = {self.denomination} \u20bd ")


if __name__ == '__main__':
    # Объект класса "Доллар"
    cur1 = Dollar(89)
    cur1.display()
    cur1.to_rubles(15)

    # Объект класса "Евро"
    cur2 = Euro(96.56)
    cur2.display()
    cur2.to_rubles(9)