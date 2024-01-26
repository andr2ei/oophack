from models import Thing, Paladin, Warrior, Person
from random import randint, sample, choice

def generate_defend_percent() -> float:
    return randint(0, 10) / 100

def generate_attack() -> int:
    return randint(0, 10)

PERSON_NAMES = [
    'Nurmagamedov',
    'Morgen',
    'Buzova',
    'Timati',
    'Shnurov',
    'Ovechckin',
    'Sobchak',
    'Basta',
    'Dzuba',
    'Gagarina',
    'Krid',
    'Kirkorov',
    'Urgant',
    'Shake',
    'Zivert',
    'Panarin',
    'Galkin',
    'Ivleeva',
    'Medvedev',
    'Bi-2'
]

PERSON_CLASSES = [Warrior, Paladin]

def generate_persons(things_box: list[Thing]) -> list[Person]:
    persons = []
    names = sample(PERSON_NAMES, 10)
    for i in range(10):
        p_class = choice(PERSON_CLASSES)
        p_name = names[i]
        p = p_class(p_name, 100.0, 20.0, 0.2)
        things = sample(things_box, randint(0, 4))
        p.set_things(things)
        persons.append(p)
    return persons

def get_things() -> list[Thing]:
    things = [
        Thing('Helmet', generate_defend_percent(), 0, hp=randint(20, 30)),
        Thing('Ring', generate_defend_percent(), randint(0, 10), hp=randint(5, 10)),
        Thing('Sword', generate_defend_percent(), randint(10, 20), hp=randint(10, 20)),
        Thing('Shield', generate_defend_percent(), 0, hp=randint(30, 40))
    ]
    things.sort(key=lambda t: t.defend_percent)
    return things

def main():

    persons = dict({(p.name, p) for p in generate_persons(get_things())})

    while len(persons.keys()) > 1:
        fighters = sample(list(persons.values()), 2)

        attacker = fighters[0]
        attack = attacker.attack()

        defender = fighters[1]
        damage = defender.calc_damage(attack)
        defender.hp_damage(damage)
        if not defender.is_alive():
            del persons[defender.name]
        print(f'{attacker} наносит удар по {defender} на {damage} урона')

    print(f'{list(persons.values())[0]} ПОБЕДИЛ!')


if __name__ == '__main__':
    main()