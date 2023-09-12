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
        self.health = 20
        self.status = "normal"

    #the functions for the commands
    def help(self, monster):
        print(">> Help <<: Brings up the action menu")
        print(">> Stats <<: brings up your stats")
        print(">> Explore <<: allows you to explore the world")
        print(">> Retreat <<: Allows you to retreat from fights")
        print(">> Fight << fight: allows you to fight monsters")
    
    #the function that displays your player stats
    def stats(self, monster):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Status: {self.status}")

    #the function that moves you from around
    def explore(self, monster):
        self.heal()
        print("Your health is now", self.health)
        if randint(0,1) == 1:
            print(monster.name, "Confronts you")
            self.status = "confronted"

    #the function to run away from a fight
    def run(self, monster):
        if randint(0, self.health) < randint(0, monster.health) :
            print('A monster has appeared')
            self.status = "confronted"
            self.fight(monster)
        else:
            self.tire()
            monster.heal()
            print("Your health suffered from running")
            print("Your health is now", self.health)

    #the function that allows you to fight monsters in the game
    def fight(self, monster):
        if self.status == "confronted":
            self.hurt()
            monster.hurt()
            print(monster.name, "attacks you")
            if self.health <= 0:
                print("You were killed by", monster.name)
            elif monster.health > 0:
                print("You survied the attack from", monster.name)
                print("Your health is now:", self.health)
            else:
                print("Victory! You defeated", monster.name)
                self.status = "normal"
        else:
            print("You are safe for now, no need to fight")

    #the kill function made for testing
    def kill(self, monster):
        self.health = 0
        print(f"{hero.name} committed suicide")

# class for all monsters
class Monster(LivingThing):
    def __init__(self, name, health):
        self.name = name
        self.health = health


#The list for all the commands
Commands = {
    "help": Player.help,
    "stats": Player.stats,
    "explore": Player.explore,
    "run": Player.run,
    "fight": Player.fight,
    "kill": Player.kill
}

#the input for the players chosen name and the title screen
print("")
name = input("Enter username \n >> ")
hero = Player(name)

#prints the welcome screen
print(" ")
print("█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀")
print("▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄")
print(" ")

#the player must type enter for the game to start
start_key = 1
while start_key > 0:
    start = input("Type enter to start \n >> ")
    if start == "enter":
        break

print(" ") #adds spce between lines


#the monsters name and stats
goblin = Monster("Goblin",20)
dragon = Monster("Dragon", 10)

#the list of monsters
monsters = []

#adding the monsters to the list
monsters.append(goblin)
monsters.append(dragon)

#choosing the monster that the plaer will face
monster = choice(monsters)

#prints the opening message to the game
print("Type help to give a list of actions")
print(hero.name, "enters a dark cave searching for adventure, you will soon face", monster.name)

#the whikle loop that will get an input for the game to continue
while hero.health > 0 and monster.health > 0:
    line = input("What do you want to do? \n >> ")
    if line in Commands.keys():
        Commands[line] (hero, monster)
    else:
        print(hero.name, "does not understand this suggestion")

print("Game Over") 
