"""This is to document this module."""

import time

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

    '''Adding a new line.'''    
    print('')



## This section will contain the game texts.

# Intro texts
intro_text1 = 'There was once a man known for his luck.'
intro_text2 = 'It is not known if the man himself was lucky, or if his dice was cursed.'
intro_text3 = 'All that is known is that this man never lost a game of dice.'
intro_text4 = 'He was called:'
intro_text5 = 'Jack D. Six'


# Gameplay texts
gameplay_1 = 'Do you want to roll the dice?'


# Game over texts
gameover_1 = 'Game over'
gameover_2 = 'The game has ended'


