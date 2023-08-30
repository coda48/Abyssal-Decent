from random import randint, choice

#The class for all living things
class LivingThing():
    #the function for the base living thing
    def __init__(self):
        self.name = "some name"
        self.health = 1
    #the function for the tire system
    def tire(self):
        self.health = self.health - 2
    #the function for the hurt system
    def hurt(self):
        self.health = self.health - randint(0, self.health)
    #the function for the heal system
    def heal(self):
        self.health = self.health + 1

#The class for the player
class Player(LivingThing):
    def __init__(self, name):
        self.name = name
        self.health = 15
        self.status = 'regular'

    #the functions for the commands
    def help(self, monster):
        pass

    def stats(self, monster):
        pass

    def explore(self, monster):
        pass

    def run(self, monster):
        pass

    def fight(self, monster):
        pass


# class for all monsters
class Monster(LivingThing):
    def __init__(self, name, health):
        self.anme = name
        self.health = health

#The list for all the commands
Commands = {
    "help": Player.help,
    "stats": Player.stats,
    "explore": Player.explore,
    "run": Player.run,
    "fight": Player.fight
}

#the input for the players chosen name
name = input("Enter username >> ")
hero = Player(name)

#the monsters name and stats
goblin = Monster("Goblin",20)
dragon = Monster("Dragon", 10)

#the list of monsters
monsters = []

#adding the monsters to the list
monsters.append(goblin)
monsters.append(dragon)

