import random
import time


def text_delay(text, delay: float):
    '''
    TODO - MAKE BETTER DOCSTRING AND PUT THE FUNCTION IN THE TEXTS FILE
    This function is used to print the text slowly, character by character
    '''
    for char in text:
        time.sleep(delay)
        print(char, end='', flush=True)


def dice_roll():
    '''
    TODO - CREATE BETTER FUNCTION (ADD MORE DICE TYPES); MAKE COMBAT FILE
    Function used to roll the dice (print random dice numbers)
    '''
    d6 = random.randint(1, 6)
    return d6


'''
TODO - PUT TEXT IN ANOTHER FILE
Text history - learn to take text from file(CSV, JSON, excel, etc)
'''
intro_text1 = 'There was once a man known for his luck.'
intro_text2 = 'It is not known if the man himself was lucky, or if his dice was cursed.'
intro_text3 = 'All that is known is that this man never lost a game of dice.'
intro_text4 = 'He was called:'
intro_text5 = 'The Dice J'


def game_start():
    '''
    TODO - CREATE GAME MENU
    Game loop; the loop will go on until the player type anything else than yes
    '''
    while True:
        '''
        TODO - PUT INTRO IN A FUNCTION (IN THE TEXTS FILE)
        '''
        text_delay(intro_text1, 0.1)
        print('')
        time.sleep(2)
        text_delay(intro_text2, 0.1)
        print('')
        time.sleep(2)
        text_delay(intro_text3, 0.1)
        print('')
        time.sleep(2)
        text_delay(intro_text4, 0.1)
        print('')
        time.sleep(3)
        text_delay(intro_text5, 1)
        print('')
        print('Do you want to roll the dice?')
        if input() == 'yes':
            print(f'You rolled a ' + str(dice_roll()))
        else:
            print('Game Over')
            break


'''
Call the game loop function
'''
game_start()
