from random import randint, choice

class LivingThing():
    def __inti__(self):
        self.name ='some name'
        self.health = 1

    def tire(self):
        self.health = self.health - 2

    def hurt(self):
        self.health = self.health - randint(0,self.health)

    def heal(self):
        self.health = self.health + 1

class Player(LivingThing):
    def __inti__(self,name):
        self.name = name
        self.health = 15
        self.status = 'regular'

    def help(self,monster):
        print('Your choices are:')
        for key in Commands.keys():
            print(key)

    def stats(self,monster):
        print('You are', self.name)
        print('With health of', self.health)
        print('Your status is', self.status)
        print(monster.name, 'health is', monster.health)

    def explore(self,monster):
        self.heal()
        print('Your health is now', self.health)
        if randint(0,1) == 1:
            print(monster.name, 'confronts you')
            print('What do you do')
            self.status = 'confronted'

    def run(self,monster):
        if randint(0,self.health) < randint(0,monster.health):
            print('A monster has appeared')
            self.stats = 'confronted'
            self.fight(monster)
        else:
            self.tire()
            monster.heal()
            print('Your health suffered by running')
            print('Your health is now', self.health)

    def fight(self,monster):
        if self.status == 'confronted':
            self.hurt()
            monster.hurt()
            print(monster.name,'attacks you')
            if self.health <= 0:
                print('You were killed by the',monster.name)
            elif monster.health > 0:
                print('You survived the', monster.name)
                print('Your health is now', self.health)
                self.status = 'regular'
            else:
                print('Victory! You defeated the', monster.name)
        else:
            print('You are safe. Not a monster in sight anywhere!')

class Monster(LivingThing):
    def __inti__(self,name,health):
        self.name = name
        self.health = health

Commands = {
    'help': Player.help,
    'stats': Player.stats,
    'explore': Player.explore,
    'run': Player.run,
    'fight': Player.fight
}

name = input('What is your name? ')
hero = Player(name)

goblin = Monster('Goblin', 20)
dragon = Monster('Dragon', 10)

monsters = []
monsters.append(goblin)
monsters.append(dragon)

monster = choice(monsters)

print(' (type help to get a list of actions) ')
print(hero.name,'enters a dark cave, searching for adventure. you will soon face the', monster.name)

while hero.health > 0 and monster.health > 0:
    line = input('What do you want to do? >>')
    if line in Commands.keys():
        Commands[line](hero,monster)
    else:
        print(hero.name,'does not understand this suggestion.')

print('Game Over')
# hehe
