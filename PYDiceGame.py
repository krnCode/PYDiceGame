import random


# Roll dice function
def dice_roll():
    d6 = random.randint(1, 6)
    return d6


# Game loop; the loop will go on until the player type anything else than 'yes'
def game_start():
    while True:
        print('Do you want to roll the dice?')
        if input() == 'yes':
            print(f'You rolled a ' + str(dice_roll()))
        else:
            print('Game Over')
            break


# Call the game loop function
game_start()
