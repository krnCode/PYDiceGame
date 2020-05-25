'''
TODO - Document EnemiesModule
'''

import random


class EnemyNormal:

    def __init__(self, name: str):
        names_enemy_humanoid = [
            'Chico', 'Manuel', 'Jonas', 'Judas', 'Zé', 'Derrick', 'Chad', 'Sam', 'Chug', 'Mary', 'Elena', 'Mack', 'Mario', 'Luigi',
            'Saad', 'Maleqiv', 'Ennis', 'Ed', 'Ned', 'Chris', 'Paul', 'Mike', 'Weiner', 'Choo', 'Chang', 'Emilia', 'Clack', 'Karen',
            'Chester', 'Ike', 'Kirby', 'Faartz', 'Lingo', 'Phoebe', 'Jesus', 'Bin', 'Kat', 'Iggy', 'Kash', 'Dick', 'Shmog', 'Maven',
            'Donald', 'Duck', 'Heisenberg', 'Guts', 'Crystal', 'Jesse', 'Pinkman', 'DJ', 'TJ', 'McMacven', 'Ronald', 'Tees', 'Hilary',
            'Domingues', 'Muerto', 'Huevos', 'McLucky', 'Walter', 'White', 'Black', 'Lee', 'Yang', 'Hoo', 'Chi', 'Janice', 'Stoppa',
            'Walberg', 'Lindus', 'Xaxa', 'Shusha', 'McLovin', 'McBurguer', 'Monsaint', 'Louis', 'Alexander', 'Vladmir', 'Yaroslav',
            'Hagar', 'Miroslav', 'Moisto', 'Ninel', 'Dazpraperma', 'Sashenka', 'Ivan', 'Ekaterina', 'Vana', 'Bete', 'Robert',
            'Georgios', 'Konstantinos', 'Chrisos', 'Basil', 'Baskem', 'Dimitris', 'Penelope', 'Arianna', 'Vania', 'Katarine', 'Zoe',
            'Sophia', 'Cora', 'Michelle', 'Michaels', 'Thea', 'Ygritte', 'Babu', 'Chelsea', 'Jovi', 'Vovs', 'Irv', 'Kdav', 'Fabu',
            'Otto', 'Zumbs', 'Korn', 'Tuka'
        ]

        titles_enemy_humanoid = [
            'The Good', 'The Bad', 'The Ugly', 'The Fat', 'The Skinny', 'The Great', 'The Awesome', 'The Champion', 'The One',
            'The Rusty', 'The Massacration', 'The Winner', 'The Loser', 'The No One', 'The Who?', 'The Whiny', 'The No Dices',
            'The Cheater', 'The Princess', 'The Queen', 'The Akhoond', 'The Priest', 'The Clerig', 'The Anchor', 'The Dux',
            'The Cond', 'The Doctor', 'The Elder', 'The Emperor', 'The Empress', 'The Man', 'The Woman', 'The Little Boy',
            'The Little Girl', 'The Generalissimo', 'The Grand Inquisitor', 'The Grand Master', 'The Guardian Immortal',
            'The Admiral', 'The Handsome Fairness', 'His Eminence', 'Her Eminence', 'The Khan', 'The Maester', 'The Legatus'
        ]

        name_first = random.choice(names_enemy_humanoid)
        name_title = random.choice(titles_enemy_humanoid)
        name_result = print(f'{name_first} "{name_title}"')

        self.name = name

        if name == '':
            name = name_result

        else:
            name = name


ze = EnemyNormal('')
ze = EnemyNormal('')
ze = EnemyNormal('')
ze = EnemyNormal('')
ze = EnemyNormal('')
ze = EnemyNormal('')

print(ze.name)
