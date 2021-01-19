"""Шаблоны проектирования."""

from abc import ABC, abstractmethod
import random

from typing import Dict, Any





class Item(ABC):
    """Абстрактный класс для итемов."""
    name = ''
    def get_item(self):
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


class MagicBookFactory(ItemFactory):
    """Конкретная фабрика для итемов."""

    def spawn_item(self):
        return MagicBook()


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
        "magicbook":MagicBookFactory,
        "totem": TotemFactory,
        "arrow": ArrowsFactory
    }
    item_list = ["sword", "bow", "apple",  "magicbook","totem","arrow"]
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
    var_type = 'Warrior'

    def attack(self, damage: int = damage):
        print('Орк атакует')
        return damage


class ArcherOrc(Enemy):
    """Класс врага орка лучника."""
    damage = Enemy.damage
    hp = Enemy.hp
    var_type = 'Archer'

    def attack(self, damage: int = damage):
        print('Орк стреляет из лука')
        return damage


class MagOrc(Enemy):
    """Класс врага орка мага."""
    damage = Enemy.damage
    hp = Enemy.hp
    var_type = 'Mag'

    def attack(self, damage: int = damage):
        print('Орк атакует магической атакой')
        return damage


class EnemyFactory(ABC):
    """Абстрактная фабрика для врага."""

    @abstractmethod
    def create_enemy(self):
        """Создание абстрактного продукта ."""
        pass


class WarriorOrcFactory(EnemyFactory):
    """Конкретная фабрика для врага."""

    def create_enemy(self):
        return WarriorOrc()


class ArcherOrcFactory(EnemyFactory):
    """Конкретная фабрика для врага."""

    def create_enemy(self):
        return ArcherOrc()


class MagOrcFactory(EnemyFactory):
    """Конкретная фабрика для врага."""

    def create_enemy(self):
        return MagOrc()

def var_spawner():
    spawner_to_factory_mapping = {
        "warriror_orc": WarriorOrcFactory,
        "archer_orc":ArcherOrcFactory,
        "mag_orc": MagOrcFactory}
    enemy_type_list = ["warriror_orc", "archer_orc", "mag_orc"]
    SPAWNER_TYPE = random.choice(enemy_type_list)
    spawner = spawner_to_factory_mapping[SPAWNER_TYPE]()
    enemy = spawner.create_enemy()
    print(f'Вы встретили врага {enemy.var_type}, с жизнями {enemy.hp} и атакой {enemy.damage}')
    return enemy

class Hero(ABC):
    """Абстрактный класс для героя."""
    name = ''
    hp = 30
    weapons_list = {'sword': 10}
    orcs_dead = 0
    hero_type = ''

    def get_weapon(self, weapon):
            """Подобрать оружие."""
            while True:
                choice = input('Введите 1 ,чтобы поднять оружие или 2, чтобы пройти мимо : ')
                if choice == '1':
                    new_weapons_list = self.weapons_list
                    new_weapons_list[weapon[0]] = weapon[1]
                    self.weapons_list = new_weapons_list
                    break
                elif choice == '2':
                    print('Вы прошли мимо')
                    break

    def hero_attack(self, weapon_list=weapons_list):
        """Атака героя."""
        temp = {}
        for i in range(len(weapon_list)):
            print(f'Нажмите {i + 1}, чтобы выбрать {list(weapon_list)[i]}')
            temp[i + 1] = list(weapon_list)[i]
        choice = input('Введите номер оружия: ')
        while True:
            if choice:
                print(f'Вы выбрали {temp[int(choice)]}, ваш инвентарь {weapon_list[temp[int(choice)]]}')
                return weapon_list[temp[int(choice)]]
            else:
                print('У вас нет оружия')

    @abstractmethod
    def special_hero(self):
        pass


class Warrior(Hero):
    """Класс воин."""

    def special_hero(self, enemy_attack: tuple):
        return "Спавн вариор", enemy_attack




class Archer(Hero):
    """Класс лучник."""

    def special_hero(self, enemy_attack: tuple):
        return "Спавн archer", enemy_attack



class Mag(Hero):
    """Класс мага."""

    def special_hero(self, enemy_attack: tuple):
        return "Спавн mag" , enemy_attack



class EnemyFactory(ABC):
    """Абстрактная фабрика для героя."""

    @abstractmethod
    def create_enemy(self):
        """Создание абстрактного продукта ."""
        pass


class WarriorHeroFactory(EnemyFactory):
    """Конкретная фабрика для героя."""

    def create_enemy(self):
        return Warrior()


class ArcherHeroFactory(EnemyFactory):
    """Конкретная фабрика для героя."""

    def create_enemy(self):
        return Archer()


class MagHeroFactory(EnemyFactory):
    """Конкретная фабрика для врага."""

    def create_enemy(self):
        return Mag()

def hero_spawner_warriror():
    spawner_to_factory_mapping = {"warriror": WarriorHeroFactory}
    spawner = spawner_to_factory_mapping["warriror"]()
    enemy = spawner.create_enemy()
    return enemy

def hero_spawner_archer():
    spawner_to_factory_mapping = {"archer": ArcherHeroFactory}
    spawner = spawner_to_factory_mapping["archer"]()
    enemy = spawner.create_enemy()
    return enemy

def hero_spawner_mag():
    spawner_to_factory_mapping = {"mag": ArcherHeroFactory}
    spawner = spawner_to_factory_mapping["mag"]()
    enemy = spawner.create_enemy()
    return enemy



while True:
    type_selector = input('Выберите класс вашего героя . 1 - воин  , 2 - лучник , 3 - маг : ')
    if type_selector == '1':
        hero = hero_spawner_warriror()
        break
    elif type_selector == '2':
        hero = hero_spawner_archer()
        break
    elif type_selector == '3':
        hero = hero_spawner_mag()
        break
    print(hero)

dead = False
while hero.orcs_dead != 10:
    random_event = random.randint(1, 2)
    if random_event == 1:
        '''Битва с монстром'''
        enemy = var_spawner()
        while True:
            choice = input('Введите 1, чтобы драться или 2, чтобы убежать : ')
            if choice == '1':
                count = 1
                while True:
                    enemy.hp = enemy.hp - hero.hero_attack()
                    if hero.hp <= 0:
                        print('')
                        print('Вы умерли')
                        dead = True
                        break
                    count += 1
                    print(f'У вас осталось - {hero.hp} жизней')
                break
            elif choice == '2':
                print('Вы сбежали')
                break

    elif random_event == 2:
        item = item_spawner()
        if item.name in ('sword', 'bow', 'magicbook'):
            print(f'Вы обнаружили {item.name} с силой - {item.attack_power}')
            hero.get_weapon(item.attack())
            print('Ваш инвентарь - ' +  str(hero.weapons_list))
        elif item.name == 'arrows':
            print('Вы обнаружили стрелы')
            hero.summary_arrows += item.attack()
        elif item.name == 'apple':
            print('ВЫ нашли яблоко')
            hero.hp += item.heal()
            print("Кол-во жизней : " + str(hero.hp))

            while True:
                choice = input('Введите 1 ,чтобы сохранится '
                               'или 2, чтобы пройти мимо : ')
                if choice == '1':
                    sleep(1)
                    hero.save_game()
                    print('Игра сохранена. Здоровье {}, Оружие {}'.format(hero.hp, hero.weapons_list))
                    break
                elif choice == '2':
                    print('Вы прошли мимо')
                    break
                else:
                    print('Вы ввели неверное значение. Введите 1 или 2')
    print(f'Орков убито {hero.orcs_dead}')
