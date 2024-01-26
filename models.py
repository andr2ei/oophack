class Thing:
    def __init__(self, name: str, defend_percent: float, attack: float, hp: float):
        self.name = name
        self.defend_percent = defend_percent
        self.attack = attack
        self.hp = hp

    def __str__(self):
        return self.name


class Person:

    def __init__(self, name: str, hp: float, base_attack: float, base_defend_percent: float):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_defend_percent = base_defend_percent
        self.final_protection: float = 0.0

    def set_things(self, things: list[Thing]):
        self.things = things.copy()

        things_defend = sum([t.defend_percent for t in self.things])
        self.final_protection = things_defend + self.base_defend_percent

        things_hp = sum([t.hp for t in things])
        self.hp += things_hp

        self.things_attack = sum([t.attack for t in things])

    def attack(self) -> float:
        return self.base_attack + self.things_attack

    def calc_damage(self, attack_damage: float):
        return (attack_damage - attack_damage * self.final_protection)

    def hp_damage(self, attack_damage: float):
        self.hp -= self.calc_damage(attack_damage)

    def is_alive(self) -> bool:
        return self.hp > 0

    def __str__(self):
        return f'{self.__class__.__name__} - {self.name}'

class Paladin(Person):
    def __init__(self, name: str, hp: float, base_attack: float, base_defend_percent: float):
        super().__init__(name, hp * 2, base_attack, base_defend_percent * 2)

class Warrior(Person):
    def __init__(self, name: str, hp: float, base_attack: float, base_defend_percent: float):
        super().__init__(name, hp, base_attack*2, base_defend_percent)