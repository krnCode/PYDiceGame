"""
TODO - Document TextsModule.
"""

import time
import random


def slow_text(text: str, delay: float):
    '''
    This function is used to display the text character by character,
    like an animation. 

    Arguments:

        text {str} -- Input the text to be applied the animation.
        delay {float} -- The time in seconds to show the next character in the text.
    '''
    for char in text:
        time.sleep(delay)
        print(char, end='', flush=True)

    '''Print a new line.'''
    print('')
    time.sleep(1)


def game_over_text():
    '''Print a random game over text from a list.'''
    game_over = random.choice(game_over_list)
    print(game_over)


# This section will contain the game texts.
# Intro texts
intro_text1 = 'There was once a man known for his luck.'
intro_text2 = 'It is not known if the man himself was lucky, or if his dice was cursed.'
intro_text3 = 'All that is known is that this man never lost a game of dice.'
intro_text4 = 'He was called:'
intro_text5 = 'Jack D. Six'


# Gameplay texts
gameplay_1 = 'Do you want to roll the dice?'


# Game over texts, in a list
game_over_list = [
    'Game over',
    'The game has ended',
    'You met your fate',
    'Your time has come',
    'Death welcomes you with open arms',
    'It was not meant to be',
    'The future refused to change',
    'Y O U    D I E D',
    'Better luck next time',
    'You woke up with the wrong foot today',
    'You run out of luck'
]

# Combat texts descriptios
combat_dice_race_description = 'DICE RACE \nGet to the desired number before your enemy'
combat_max_roll_description = 'MAX ROLL \nGet a higher number than your enemy'
combat_min_roll_description = 'MINIMUM ROLL\nGet a lesser number than your enemy'
combat_excact_number_description = 'EXACT NUMBER \nRoll the dice until you get the exact number'
combat_cant_be_description = 'CAN\'T BE \nGet to the desired number, but following a determined set of rules'
combat_mortal_dice_description = 'MORTAL DICE \nEach number you roll will be the damage you deal to your enemy.'
