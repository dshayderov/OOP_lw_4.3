#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный номер объекта,
и свойство, в котором хранится принадлежность команде. У солдат есть метод "иду за героем", который в
качестве аргумента принимает объект типа "герой". У героев есть метод увеличения собственного уровня.
В основной ветке программы создается по одному герою для каждой команды. В цикле генерируются объекты-солдаты.
Их принадлежность команде определяется случайно. Солдаты разных команд добавляются в разные списки.
Измеряется длина списков солдат противоборствующих команд и выводится на экран. У героя, принадлежащего
команде с более длинным списком, увеличивается уровень.
Отправьте одного из солдат первого героя следовать за ним. Выведите на экран идентификационные номера этих двух юнитов.
"""

import random


class Character:

    def __init__(self, id, team):
        self.id = int(id)
        self.team = team


class Soldier(Character):

    # Метод "иду за героем"
    def follow_the_hero(self, hero):
        print(f"Солдат {self.id} следует за героем {hero.id}")


class Hero(Character):

    def __init__(self, id, team, level=1):
        super().__init__(id, team)
        self.level = level

    # Метод увеличения собственного уровня
    def level_up(self):
        self.level += 1
        print(f"Герой {self.id} достиг уровня {self.level}")


if __name__ == '__main__':
    # Создание героев
    hero_1 = Hero(1, 'Team_1')
    hero_2 = Hero(2, 'Team_2')

    # Создание солдат для каждой команды
    soldiers_team_1 = [Soldier(random.randint(3, 50), 'Team_1') for i
                       in [1] * random.randint(5, 15)]
    print(f"В первой команде {len(soldiers_team_1)} солдат")

    soldiers_team_2 = [Soldier(random.randint(51, 99), 'Team_2') for i
                       in [1] * random.randint(5, 15)]
    print(f"Во второй команде {len(soldiers_team_2)} солдат")

    # Сравнение количества солдат в команде
    if len(soldiers_team_1) > len(soldiers_team_2):
        hero_1.level_up()
    elif len(soldiers_team_2) > len(soldiers_team_1):
        hero_2.level_up()
    else:
        r = random.choice([1, 2])
        if r == 1:
            soldiers_team_1.append(Soldier(100, 'Team_1'))
        else:
            soldiers_team_2.append(Soldier(100, 'Team_2'))

    # Солдат первого героя отправлен следовать за ним
    random_unit = random.choice(soldiers_team_1)
    random_unit.follow_the_hero(hero_1)
