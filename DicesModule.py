'''
This module contains all the dice functions for the game. The dices can be interpreted as 'weapons', since it is the only thing you use to confront enemies. 
'''

import random


def d6_roll():
    d6 = random.randint(1, 6)
    return d6


def d8_roll():
    d8 = random.randint(1, 8)
    return d8


def d10_roll():
    d10 = random.randint(1, 10)
    return d10


def d12_roll():
    d12 = random.randint(1, 12)
    return d12


def d20_roll():
    d20 = random.randint(1, 20)
    return d20
