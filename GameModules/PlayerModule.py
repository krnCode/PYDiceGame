'''
TODO - Document PlayerModule
'''

import random


class PlayerCharacter:
    '''
    TODO - Document the class
    '''

    def __init__(self, name: str):
        names_player_first = [
            'Jack', 'James', 'Jesse', 'Igor', 'Anabelle', 'Alice', 'Maria', 'Antonio', 'Nori', 'Lucas', 'Mary', 'Isa', 'Isaac',
            'Dick', 'Bonnie', 'Aysha', 'Fleur', 'Harry', 'Ivan', 'Sienna', 'Elizabeth', 'Claudia', 'Silvana', 'Ale', 'Vera', 'Cris',
            'Val', 'Jon', 'Tyrion', 'Jaime', 'Khal', 'Cersei', 'Gregor', 'Ramsay', 'Joffrey', 'Robb', 'Ned', 'Sandor', 'Mel', 'Brienne',
            'Tormund', 'Oberyn', 'Bronn', 'Margery', 'Hodor', 'Jaqen', 'Tyene', 'Samwell', 'Tywin', 'Hermione', 'Ronald', 'Severus',
            'Draco', 'Luna', 'Belatriz', 'Dolores', 'Remo', 'Cho', 'Lucio', 'Alastor', 'Petúnia', 'Molly', 'Daario', 'No', 'Petyr',
            'Jojen', 'Robert', 'Walder', 'Long', 'Johnson', 'Shlong', 'Puss', 'Hairy', 'Lady Bits', 'Poon', 'Smoo', 'Rabbit', 'Roger',
            'Arthur', 'Boring', 'Lara', 'Boiled', 'Samus', 'Solid', 'Liquid', 'Master', 'Nathan', 'Marcus', 'Ezio', 'Jil', 'John', 'Ryu',
            'Agent', 'Niko', 'Duke', 'Sam', 'Sarah', 'Venom', 'Fox', 'Alucard', 'Jim', 'Cat', 'Dog', 'Pierce', 'Xuxa', 'Sky', 'Monkey'
        ]

        names_player_last = [
            'Targaryen', 'Snow', 'Stark', 'Lannister', 'Clegane', 'Greyjoy', 'Black', 'Naharis', 'One', 'Giantsbane', 'Martell', 'Baelish',
            'H\'ghar', 'Sand', 'Reed', 'Tally', 'Baratheon', 'Tyrell', 'Bolton', 'Frey', 'Granger', 'Weasley', 'Potter', 'Lovegood',
            'McGonagall', 'Malfoy', 'Snape', 'Lupin', 'Lestrange', 'Chang', 'Delacour', 'Evans', 'Moody', 'Dick', 'Big', 'Mini', 'Wet',
            'Hard', 'Soft', 'Neverup', 'Alwayshigh', 'Dry', 'Dong', 'Shlong', 'Ladybits', 'Poon', 'Smoo', 'Sunny', 'Rainy', 'Deep'
            'Caerbannog', 'Shrubber', 'Nudge', 'Prophet', 'Groins', 'Eggs', 'Croft', 'Aran', 'Solid', 'Liquid', 'Chief', 'Drake', 'Fenix',
            'Firenze', 'Valentine', 'Marston', 'Hayabuza', '47', 'Belic', 'Nukem', 'Fisher', 'Kerrigan', 'Boss', 'Bossman', 'McCloud',
            'Midnight', 'Morrison', 'Raynor', 'Cat', 'Dog', 'Brosnan', 'Bond', 'Meneghel', 'Rim', 'Inside', 'Hodor', 'Luffy', 'Joanna',
            'Resenha', 'Momma', 'Pappa'
        ]

        names_player_middle = [
            'The Cheater', 'Allsix', 'Double Six', 'Sixsided', 'Luck', 'Four Leaf Clover', 'Fortune', 'Good Job', 'Nice Roll', 'The Roller',
            'Dice\'n\'Mice', 'Winning', 'Big Pockets', 'Full Pockets', 'Bets On', 'Wager', 'All Right', 'Feeling It', 'Again', 'Oldman',
            'Prophet', 'That Guy', 'That Girl', 'Karen', 'Drama Queen', 'Oldlady', 'Bad Mouth', 'Strange', 'Doorbel', 'Awaken', 'Wake',
            'The Midnight', 'The Beast', 'The Vampire', 'The Angel', 'Queen', 'Princess', 'The Ruler', 'Commander', 'Strategist', 'Mage',
            'The Rainmaker', 'Anon', 'Midget', 'The Fairy', 'The Legend', 'Killer', 'The Saint', 'The Demon', 'The Ogre', 'The Super',
            'The Ultra', 'Combo', 'Mad Respect', 'Thief', 'Survivor', 'The Brains', 'Canon', 'Fatality', 'The End', 'The Chad',
            'Barrel Roll', 'Unlimited', 'The Scientist', 'The Traveller', 'The Normal', 'Not a Fan of Celebrities', 'Never Eat Vegetables',
            'Need a Shower', 'Release the Kraken', 'Fartmouth', 'Monoeyebrowns', 'The One', 'The No One', 'Beggar', 'Should Never Come Here',
            'You\'re Finally Awake', 'The Meow', 'The Woof', 'I Can\'t Even', 'Should Have Stayed At Home Playing Video-Games', 'More Mayo',
            'The Mustard', '007', 'Hodor', 'The Code', 'Codex', 'Alpha', 'Beta', 'D.', 'Dead', 'Wit', 'Furball', 'Big Enough for Two',
            'Kick in The Eggs', 'Big Head', 'Small Brains', 'Shaken', 'Animal', 'Oh Yeah', 'So Long', 'Not a Guy', 'Not a Girl', 'Mandman',
            'Madwoman', 'Marijuana', 'Cocaine', 'The Pox', 'Shake It', 'Divine', 'Gimme', 'Elevated', 'Dream', 'Hollow', 'Kick Inda',
            'The Inside', 'Mommy', 'Daddy'
        ]

        name_first = random.choice(names_player_first)
        name_middle = random.choice(names_player_middle)
        name_last = random.choice(names_player_last)
        name_result = print(f'{name_first} "{name_middle}" {name_last}')

        self.name = name

        if name == '':
            name = name_result

        else:
            name = name

        self.life = 100
        self.dices = 3
