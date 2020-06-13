'''
TODO - Document CombatModule
'''

import random
import TextsModule as TexMod
import DicesModule as DiceMod


class CombatType:

    def __init__(self, combat_type):
        self.combat_type = combat_type
        types_of_combat = [
            'Dice Race',
            'Max Roll',
            'Minimum Roll',
            'Exact Number',
            'Can\'t Be',
            'Mortal Dice',
        ]
        combat_style = random.choice(types_of_combat)

        if combat_type == '':
            combat_style = random.choice(types_of_combat)
            combat_type = combat_style

        else:
            combat_type = combat_type


class CombatDiceRace:

    def __init__(self, race_lenght: int):
        self.description = TexMod.combat_dice_race_description
        self.race_lenght = race_lenght

        if race_lenght == '':
            race_gen = random.randint(10, 100)
            race_lenght = print(race_gen)

    def combat_play(self):
        self.race_start = 0
        self.race_player_start_score = 0
        self.race_enemy_start_score = 0

        while True:
            print(TexMod.gameplay_1)
            if input() == 'yes':
                player_roll = DiceMod.dice_roll('d6')
                print(player_roll)

        else:
            print('game over')
