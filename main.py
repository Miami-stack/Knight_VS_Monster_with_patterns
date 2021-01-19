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


class Item(ABC):
    """Абстрактный класс для итемов."""
    name = ''
    def get_item(self):
        """Take item"""
        return self


class Sword(Item):
    """  Меч."""
    attack_power = random.randint(1, 20)
    name = 'sword'
    def attack(self, attack_power: int = attack_power):
        return 'sword', attack_power


class Bow(Item):
    """Лук."""
    attack_power = random.randint(1, 20)
    name = 'bow'
    def attack(self, attack_power: int = attack_power):
        return 'Bow', attack_power


class Arrows(Item):
    """Стрелы."""
    arrows = random.randint(1, 20)
    name = 'arrows'
    attack_power = 0
    def attack(self, additional_arrows: int = arrows):
        return additional_arrows


class MagicBook(Item):
    """Магическая книга."""
    attack_power = random.randint(1, 20)
    name = 'magic book'
    def attack(self, attack_power: int = attack_power):
        return "Magic book", attack_power


class Apple(Item):
    """Яблоко."""
    name = 'apple'
    attack_power = 0
    def heal(self):
        return random.randint(1, 20)


class Totem(Item):
    """Создание тотема."""
    name = 'totem'
    attack_power = 0


class ItemFactory(ABC):
    """Абстрактная фабрика для итемов."""

    @abstractmethod
    def spawn_item(self):
        """Создание абстрактного продукта."""
        pass


class SwordFactory(ItemFactory):
    """Конкретная фабрика для итемов."""

    def spawn_item(self):
        return Sword()


class BowFactory(ItemFactory):
    """Конкретная фабрика для итемов."""

    def spawn_item(self):
        return Bow()


class SpellBookFactory(ItemFactory):
    """Конкретная фабрика для итемов."""

    def spawn_item(self):
        return SpellBook()


class AppleFactory(ItemFactory):
    """Конкретная фабрика для итемов."""

    def spawn_item(self):
        return Apple()


class TotemFactory(ItemFactory):
    """"Конкретная фабрика для итемов."""

    def spawn_item(self):
        return Totem()


class ArrowsFactory(ItemFactory):
    """Конкретная фабрика для итемов."""

    def spawn_item(self):
        return Arrows()

def item_spawner():
    """Спавнер."""
    spawner_to_factory_mapping = {
        "sword": SwordFactory,
        "bow":BowFactory,
        "apple": AppleFactory,
        "spellbook":SpellBookFactory,
        "totem": TotemFactory,
        "arrow": ArrowsFactory
    }
    item_list = ["sword", "bow", "apple",  "spellbook","totem","arrow"]
    SPAWNER_TYPE = random.choice(item_list)
    spawner = spawner_to_factory_mapping[SPAWNER_TYPE]()
    item = spawner.spawn_item()
    return item


class Enemy(ABC):
    """Абстрактный класс для врагов."""
    damage = random.randint(5, 10)
    hp = random.randint(20, 50)
    var_type = ''
    @abstractmethod
    def attack(self, damage=damage):
        pass


class WarriorOrc(Enemy):
    """Класс врага орка воина."""
    damage = Enemy.damage
    hp = Enemy.hp
    var_type = 'ORC'

    def attack(self, damage: int = damage):
        print('Орк атакует')
        return damage, 'melee'


class ArcherOrc(Enemy):
    """Класс врага орка лучника."""
    damage = Enemy.damage
    hp = Enemy.hp
    enemy_type = 'ELF'

    def attack(self, damage: int = damage):
        print('Орк стреляет из лука')
        return damage, 'range'


class MagOrc(Enemy):
    """Класс врага орка мага."""
    damage = Enemy.damage
    hp = Enemy.hp
    enemy_type = 'WARLOCK'

    def attack(self, damage: int = damage):
        print('Орк атакует магической атакой')
        return damage, 'spell'


class EnemyFactory(ABC):
    """Абстрактная фабрика для врага."""

    @abstractmethod
    def create_enemy(self):
        """Создание абстрактного продукта ."""
        pass


class WarriorOrcFactory(EnemyFactory):
    """Конкретная фабрика для врага."""

    def create_enemy(self):
        return Orc()


class ArcherOrcFactory(EnemyFactory):
    """Конкретная фабрика для врага."""

    def create_enemy(self):
        return AngryElf()


class MagOrcFactory(EnemyFactory):
    """Конкретная фабрика для врага."""

    def create_enemy(self):
        return Warlock()

def spawner():
    spawner_to_factory_mapping = {
        "warriror_orc": WarriorOrcFactory,
        "archer_orc":ArcherOrcFactory,
        "mag_orc": MagOrcFactory}
    enemy_type_list = ["warriror_orc", "archer_orc", "mag_orc"]
    SPAWNER_TYPE = random.choice(enemy_type_list)
    spawner = spawner_to_factory_mapping[SPAWNER_TYPE]()
    enemy = spawner.create_enemy()
    print(f'Вы встретили врага {enemy.enemy_type}, с жизнями {enemy.hp} и атакой {enemy.damage}')
    return enemy


