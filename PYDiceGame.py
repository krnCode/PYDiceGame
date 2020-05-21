import TextsModule as TexMod
import DicesModule as DicMod
import time

def game_start():
    '''Main game loop'''

    while True:
        '''Intro of the game'''        
        TexMod.slow_text(TexMod.intro_text1, 0.1)
        time.sleep(1)
        TexMod.slow_text(TexMod.intro_text2, 0.1)
        time.sleep(1)
        TexMod.slow_text(TexMod.intro_text3, 0.1)
        time.sleep(1)
        TexMod.slow_text(TexMod.intro_text4, 0.1)
        time.sleep(1)
        TexMod.slow_text(TexMod.intro_text5, 1)
        time.sleep(1)
        print(TexMod.gameplay_1)

        if input() == 'yes':
            print(f'You rolled a ' + str(DicMod.dice_roll()))
        
        else:
            print('Game Over')
            break


'''Call the game loop function'''
game_start()
