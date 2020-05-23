'''
This module contains all the dice classes for the game.
The dices can be interpreted as 'weapons', since it is
the only thing you use to confront enemies. 
'''

import random


class DicesNormal:
    '''
    Defines the class DicesNormal, the normal 'weapons' in the game.
    TODO - Better documentation of the class.
    '''
    # Class atributes
    type_of_equip = 'Weapon'
    type_of_damage = 'Neutral'
    type_of_luck = 'Normal'

    # Class instances attributes
    def __init__(self, equip: str, damage: str, luck: float):
        self.equip = equip
        self.damage = damage
        self.luck = luck

    # Class instance methods
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
