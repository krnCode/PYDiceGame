'''
TODO - Document CombatModule
'''

import random


class Combat:

    def __init__(self, combat_type, combat_turns):
        self.combat_type = combat_type
        combat_type = [
            'Dice Race',
            'Max Roll',
            'Minimum Roll',
            'Exact Number',
            'Can\'t be Number',
            '',
        ]
