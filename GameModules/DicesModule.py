'''
TODO - Document DicesModule.
'''

import random


class DicesNormal:

    def __init__(self, damage: str):
        self.damage = damage

    def description(self):
        return f'A normal type of dice.\n'
        'EQUIP: {DicesNormal.type_of_equip}\n'
        'DAMAGE: {DicesNormal.type_of_damage}\n'
        'LUCK: {DicesNormal.type_of_luck}'

    def dice_roll(self, damage):
        if damage == 'd6':
            d6 = random.randint(1, 6)
            return d6

        if damage == 'd8':
            d8 = random.randint(1, 8)
            return d8

        if damage == 'd10':
            d10 = random.randint(1, 10)
            return d10

        if damage == 'd12':
            d12 = random.randint(1, 12)
            return d12

        if damage == 'd20':
            d20 = random.randint(1, 20)
            return d20
