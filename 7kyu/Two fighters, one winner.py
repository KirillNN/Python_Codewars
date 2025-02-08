class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)

    __repr__ = __str__


def declare_winner(fighter1: Fighter, fighter2: Fighter, first_attacker: str) -> str:
    fighters = [fighter2, fighter1]
    if fighter1.name == first_attacker:
        fighters = [fighter1, fighter2]

    while fighter1.health * fighter2.health > 0:
        fighters[1].health -= fighters[0].damage_per_attack
        fighters[0], fighters[1] = fighters[1], fighters[0]

    return fighters[1].name


print(declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew"))
