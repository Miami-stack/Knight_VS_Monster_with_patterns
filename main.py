"""Шаблоны проектирования."""

from abc import ABC, abstractmethod
import random

from typing import Dict, Any


def false_input(values: list) -> int:
    """Проверка введенного значения с клавиатуры."""
    while True:
        try:
            value = int(input())
        except ValueError:
            print("Надо ввести 1 или 2 ")
            continue



class Items:
    """Класс создающий итемы."""

    def __init__(self) -> None:
        """Конструктор названий итемов."""
        self.name = name

    def get_name(self, name=None) -> str:
        """Присваивает название итемам."""
        return self.name

    def __str__(self) -> str:
        """Создает название итемов."""
        return self.name


class Equipment(Items):
    """Класс создающий итемы для атаки."""

    def __init__(self) -> None:
        """Конструктор атаки."""
        super().__init__()
        self.damage = damage

    def get_damage(self, damage=0) -> int:
        """Возвращает число атаки."""
        return self.damage

    def __str__(self) -> str:
        """Выводит число урона."""
        return self.name + " урон: " + str(self.damage)


class Sword(Equipment):
    """Класс создающий итем меч."""

    def __init__(self, d: int) -> None:
        """Конструктор меча."""
        super().__init__()
        self.damage = d
        self.name = "Меч"


class Bow(Equipment):
    """Класс создающий итем лук."""

    def __init__(self, d: int) -> None:
        """Конструктор лука."""
        super().__init__()
        self.damage = d
        self.name = "Лук"


class Arrows(Equipment):
    """Класс создающий итем стрелы."""

    def __init__(self, d: int) -> None:
        """Конструктор стрел."""
        super().__init__()
        self.damage = damage_arrows
        self.name = "Стрелы"


class MagicBook(Equipment):
    """Класс создающий итем магическая книга."""

    def __init__(self, d: int) -> None:
        """Конструктор магической книги."""
        super().__init__()
        self.damage = damage_magic
        self.name = "Магическая книга"


class Apple(Items):
    """Класс создающий итем яблоко."""

    def __init__(self) -> None:
        """Конструктор яблока."""
        super().__init__()
        self.name = "Яблоко"
        self.heal = heal


class Totem(Items):
    """Класс создающий итем тотем."""

    def __init__(self) -> None:
        """Конструктор тотема."""
        super().__init__()
        self.name = "Тотем"
        self.state_health = None
        self.items = Dict[str, Equipment]
        self.enemy_win_count = None


class Character(ABC, Equipment):
    """Абстрактный класс персонажа."""

    def __init__(self) -> None:
        """Конструктор персонажа."""
        super().__init__()
        self.state_health = 10
        self.items = {"Sword": None,
                      "Magic_book": None,
                      "Bow": None,
                      "Arrows": None}
        self.totem = None
        self.enemy_win_count = 0

    def attack(self, type_weapon) -> Any:
        """Количества нанесенного урона."""
        pass

    def take_weapon(self, weapon: Equipment) -> None:
        """Добавления оружия в инвентарь рыцаря."""
        if isinstance(weapon, Sword):
            self.items['Sword'] = weapon
        if isinstance(weapon, Bow):
            self.items['Bow'] = weapon
        if isinstance(weapon, Arrows):
            self.items['Arrows'] = weapon
        if isinstance(weapon, MagicBook):
            self.items['Magic_book'] = weapon

    def get_inventory_string(self) -> str:
        """Какие вещи хранятся в инвентаре."""
        st = "В инвентаре есть   " + '   '
        for k, item in self.items.items():
            if item is not None:
                st += str(item)
        if self.totem is not None:
            st += str(self.totem)
        return st

    def __str__(self) -> str:
        """Отображение данных о персонаже."""
        return "Здоровье персонажа " + str(self.state_health) + '   ' + "Побеждено врагов: " \
               + str(self.enemy_win_count) + self.get_inventory_string()

    def get_available_weapons(self) -> list:
        """Выбор оружия."""
        weaponless = []
        if self.items["Sword"] is not None:
            weaponless.append(self.items["Sword"])
        if self.items["Magic_book"] is not None:
            weaponless.append(self.items["Magic_book"])
        if self.items["Bow"] is not None and self.items["Arrows"] is not None:
            weaponless.append(self.items["Bow"])
        return weaponless

    def save_to_totem(self) -> None:
        """Сохранение при поднятии тотема."""
        totem = Totem()
        totem.state_health = self.state_health
        totem.items = self.items.copy()
        totem.enemy_win_count = self.enemy_win_count
        self.totem = totem

    def restore_from_totem(self) -> None:
        """Восстановление из тотема."""
        self.state_health = self.totem.state_health
        self.items = self.totem.items
        self.enemy_win_count = self.totem.enemy_win_count
        self.totem = None


class Wizard(Character):
    """Рыцарь класса маг."""

    def attack(self, type_weapon: str = "Magic_book") -> Any:
        """Аттака класса маг."""
        if type_weapon == "Magic_book":
            self.attack(type_weapon)

    def __str__(self) -> str:
        """вывод атаки."""
        return "класс маг" + str(super().__str__())


class Archer(Character):
    """Рыцарь класса лучник."""

    def attack(self, type_weapon: str = "Bow") -> Any:
        """Аттака класса лучник."""
        if type_weapon == "Bow":
            self.attack(type_weapon)

    def __str__(self) -> str:
        """вывод атаки."""
        return "класс лучник\n" + str(super().__str__())


class Knight(Character):
    """Рыцарь класса воин."""

    def attack(self, type_weapon: str = "Sword") -> Any:
        """Атака класса воин."""
        if type_weapon == "Sword":
            self.attack(type_weapon)

    def __str__(self) -> str:
        """вывод атаки."""
        return "класс воин" + str(super().__str__())


class CharacterFactory(ABC):
    """Абстрактная фабрика рыцаря."""

    @abstractmethod
    def create_character(self, weapon: Equipment = None) -> Character:
        """Создание рыцарей из абстрактной фабрики."""
        pass


class WizardFactory(CharacterFactory):
    """Конкретная фабрика рыцаря маг."""

    def create_character(self, weapon: Equipment = None) -> Wizard:
        """Создание рыцаря маг."""
        wizard = Wizard()
        if weapon is None:
            wizard.take_weapon(Sword(10))
        else:
            wizard.take_weapon(weapon)
        return wizard


class ArcherFactory(CharacterFactory):
    """Конкретная фабрика рыцаря лучник."""

    def create_character(self, weapon: Equipment = None) -> Archer:
        """Создание рыцаря лучник."""
        archer = Archer()
        if weapon is None:
            archer.take_weapon(Sword(10))
        else:
            archer.take_weapon(weapon)
        return archer


class KnightFactory(CharacterFactory):
    """Конкретная фабрика рыцаря воин."""

    def create_character(self, weapon: Equipment = None) -> Knight:
        """Создание рыцаря воин."""
        knight = Knight()
        if weapon is None:
            knight.take_weapon(Sword(10))
        else:
            knight.take_weapon(weapon)
        return knight


def set_choose() -> Any:
    """Перебор элементов, если они существуют."""
    if isinstance(select_weapon, Sword):
        print("Sword")
    if isinstance(select_weapon, Bow):
        print("Bow")
    if isinstance(select_weapon, MagicBook):
        print("Magic_book")
    else:
        print("пусто")


spawner_to_factory_mapping = {"Knight": KnightFactory(),
                              "Archer": ArcherFactory(),
                              "Wizard": WizardFactory()}
hero_type_list = ["Knight", "Archer", "Wizard"]
print("Выбираем класс игрока")
menu_items = []
for i in range(len(hero_type_list)):
    print(str(i + 1) + ". " + str(hero_type_list[i]))
    menu_items.append(i + 1)
a = false_input(menu_items)
hero = spawner_to_factory_mapping[hero_type_list[a - 1]].create_character(Sword(10))
hero.state
_health = 10
print("Вы выбрали персонажа:" + '   ' + str(hero))

while True:
    eauqipment_weapon = []
    choose = random.choice(['1', '2', '3', '4'])
    equipment_type = random.choice(["Sword", "Bow", "Arrows", "Magic_book"])
    if choose == '1':
        if equipment_type == "Sword":
            equipment = Sword(random.randrange(3, 20))
            print("Вы нашли предмет: ")
            print(equipment)
            print("1 - Подобрать предмет, 2 - Пройти мимо")
            fl = false_input([1, 2])
            if fl == 1:
                eauqipment_weapon.append(hero.take_weapon(equipment))
                print("Вы подобрали предмет " + str(equipment))
        if equipment_type == "Bow":
            equipment = Bow(random.randrange(3, 20))
            print("Вы нашли предмет: ")
            print(equipment)
            print("1 - Подобрать предмет, 2 - Пройти мимо")
            fl = false_input([1, 2])
            if fl == 1:
                eauqipment_weapon.append(hero.take_weapon(equipment))
                print("Вы подобрали предмет " + str(equipment))
        if equipment_type == "Arrows":
            equipment = Arrows(random.randrange(3, 20))
            print("Вы нашли предмет: ")
            print(equipment)
            print("1 - Подобрать предмет, 2 - Пройти мимо")
            fl = false_input([1, 2])
            if fl == 1:
                eauqipment_weapon.append(hero.take_weapon(equipment))
                print("Вы подобрали предмет " + str(equipment))
        if equipment_type == "Magic_book":
            equipment = MagicBook(random.randrange(3, 20))
            print("Вы нашли предмет: ")
            print(equipment)
            print("1 - Подобрать предмет, 2 - Пройти мимо")
            fl = false_input([1, 2])
            if a == 1:
                eauqipment_weapon.append(hero.take_weapon(equipment))
                print("Вы подобрали предмет " + str(equipment))
    if choose == '2':
        print("Вы встретили врага, Каким оружием вы хотите атаковать врага?")
        weapons = hero.get_available_weapons()
        menu_items = []
        for i in range(0, len(weapons)):
            menu_items.append(i + 1)
            print(str(i + 1) + " " + str(weapons[i]))
        fl = false_input(menu_items)
        select_weapon = weapons[a - 1]
        devil_type = random.choice(["Knight", "Archer", "Wizard"])
        devil = spawner_to_factory_mapping[devil_type].create_character()
        print("Вы встретили врага: " + str(devil) + '  ' + "1 - Сразиться, 2 - Убежать")
        fl = false_input([1, 2])
        if fl == 1:
            while hero.state_health > 0 or hero.state_health != 0 \
                    and devil.state_health > 0 or devil.state_health != 0:
                devil.state_health = hero.state_health - devil.state_health
                print("Здоровье монстра: " + str(devil.state_health))

    if choose == '3':
        print("Вы нашли тотем: 1 - Подобрать, 2 - Пройти мимо")
        fl = false_input([1, 2])
        if fl == 1:
            hero.save_to_totem()
        print("Сохранили игру")
