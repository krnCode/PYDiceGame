import TextsModule as TexMod
import DicesModule as DicMod
import time


def game_start():
    '''Main game loop'''

    while True:
        '''Intro of the game'''
        # TexMod.slow_text(TexMod.intro_text1, 0.1)
        # TexMod.slow_text(TexMod.intro_text2, 0.1)
        # TexMod.slow_text(TexMod.intro_text3, 0.1)
        # TexMod.slow_text(TexMod.intro_text4, 0.1)
        # TexMod.slow_text(TexMod.intro_text5, 1)
        print(TexMod.gameplay_1)

        if input() == 'yes':
            print(f'You rolled a ' + str(DicMod.d6_roll()))

        else:
            return TexMod.game_over_text()
            break


'''Call the game loop function'''
game_start()
