class Weapon:
    def __init__(self, name, damage, range_):
        self.__name = name
        self.__damage = damage
        self.__range_ = range_

    def hit(self, actor, target):
        pass

    def __str__(self):
        return self.__name

    @property
    def damage(self):
        return self.__damage

    @property
    def range_(self):
        return self.__range_


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__hp = hp

    def move(self, delta_x, delta_y):
        self.__pos_x += delta_x
        self.__pos_y += delta_y

    def is_alive(self):
        return True if self.__hp > 0 else False

    def get_damage(self, amount):
        self.__hp -= amount

    def get_coords(self):
        return self.__pos_x, self.__pos_y


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.__weapon = weapon

    def hit(self, target):
        if isinstance(target, MainHero):
            x1, y1 = self.get_coords()
            x2, y2 = target.get_coords()
            if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= self.__weapons.range_:
                if target.is_alive():
                    target.get_damage(self.__weapons.damage)
                    print(
                        f'Главному персонажу нанесен урон оружием {self.__weapons[self.__wind]} в размере {self.__weapons[self.__wind].damage}')
                else:
                    print('Главный персонаж уже повержен')
            else:
                print(f'Главный персонаж слишком далеко для оружия {self.__weapons}')
        else:
            print('Могу ударить только Главного героя')

    def __str__(self):
        return f'Враг на позиции {self.__pos_x, self.__pos_y} с оружием {self.__weapon}'


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.__name = name
        self.__weapons = list()
        self.__wind = None

    def hit(self, target):
        if self.__weapons == list():
            print('Я безоружен')
        elif isinstance(target, BaseEnemy):
            x1, y1 = self.get_coords()
            x2, y2 = target.get_coords()
            if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= self.__weapons[self.__wind].range_:
                if target.is_alive():
                    target.get_damage(self.__weapons[self.__wind].damage)
                    print(
                        f'Врагу нанесен урон оружием {self.__weapons[self.__wind]} в размере {self.__weapons[self.__wind].damage}')
                else:
                    print('Враг уже повержен')
            else:
                print(f'Враг слишком далеко для оружия {self.__weapons[self.__wind]}')
        else:
            print('Могу ударить только врага')

    def add_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.__weapons.append(weapon)
            if len(self.__weapons) == 1:
                self.__wind = 0
            print(f'Подобрал оружие: {weapon}')
        else:
            print('Это не оружие')

    def next_weapon(self):
        if self.__weapons == list():
            print('Я безоружен')
        elif len(self.__weapons) == 1:
            print('У меня только одно оружие')
        else:
            self.__wind = (self.__wind + 1) % len(self.__weapons)
            print(f'Сменил оружие на {self.__weapons[self.__wind]}')

    def health(self, amount):
        self.__hp += amount
        if self.__hp > 200:
            self.__hp = 200
        print(f'Полечился, теперь здоровья {self.__hp}')


if __name__ == '__main__':
    weapon1 = Weapon('Короткий меч', 5, 1)
    weapon2 = Weapon('Длинный меч', 7, 2)
    weapon3 = Weapon('Лук', 3, 10)
    weapon4 = Weapon('Лазерная орбитальная пушка', 1000, 1000)
    princess = BaseCharacter(100, 100, 100)
    archer = BaseEnemy(50, 50, weapon3, 100)
    armored_swordman = BaseEnemy(10, 10, weapon2, 500)
    archer.hit(armored_swordman)
    armored_swordman.move(10, 10)
    print(armored_swordman.get_coords())
    main_hero = MainHero(0, 0, 'Король артур', 200)
    main_hero.hit(armored_swordman)
    main_hero.next_weapon()
    main_hero.add_weapon(weapon1)
    main_hero.hit(armored_swordman)
    main_hero.add_weapon(weapon4)
    main_hero.hit(armored_swordman)
    main_hero.next_weapon()
    main_hero.hit(princess)
    main_hero.hit(armored_swordman)
    main_hero.hit(armored_swordman)
