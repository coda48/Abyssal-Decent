from random import randint, choice

#The class for all living things
class LivingThing():
    #the function for the base living thing
    def __init__(self):
        self.name = " "
        self.health = 1
    #the function for the tire system
    def tire(self):
        self.health = self.health - 2
    #the function for the hurt system
    def hurt(self):
        self.health = self.health - randint(0, self.health)
    #the function for the heal system
    def regen(self):
        self.health = self.health + 1

#The class for the player
class Player(LivingThing):
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.rest_count = 10
        self.status = "normal"

    #the functions for the commands
    def help(self, monster):
        print(">> Help <<: Brings up the action menu")
        print(">> Stats <<: brings up your stats")
        print(">> Explore <<: allows you to explore the world")
        print(">> Retreat <<: Allows you to retreat from fights")
        print(">> Fight <<: fight: allows you to fight monsters")
    
    #the function that displays your player stats
    def stats(self, monster):
        print(f">> Name: {self.name} <<")
        print(f">> Health: {self.health} <<")
        print(f">> Status: {self.status} <<")
        print(f">> Time before rest {self.rest_count} <<")

    #the function that moves you from around
    def explore(self, monster):
        self.regen()
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
            monster.regen()
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
                print(f"The monsters health is now: {monster.health}")
            else:
                print("Victory! You defeated", monster.name)
        else:
            print("You are safe for now, no need to fight")

    #the kill function made for testing
    def kill(self, monster):
        self.health = 0
        print(f"{hero.name} committed suicide")

    #the rest system for when you get tired
    def rest(self, monster):
        if self.rest_count == 0:
            self.rest_count = 10
            print("You have had a good night sleep, you are now fully rested")
        else:
            print("You do not need to rest right now")

# class for all monsters
class Monster(LivingThing):
    def __init__(self, name, health):
        self.name = name
        self.health = health

#the credits for when the game ends
def credits():
    print(" ")
    print("▀█▀ █░█ ▄▀█ █▄░█ █▄▀ █▀   █▀▀ █▀█ █▀█   █▀█ █░░ ▄▀█ █▄█ █ █▄░█ █▀▀")
    print("░█░ █▀█ █▀█ █░▀█ █░█ ▄█   █▀░ █▄█ █▀▄   █▀▀ █▄▄ █▀█ ░█░ █ █░▀█ █▄█")
    print(" ")


#The list for all the commands
Commands = {
    "help": Player.help,
    "stats": Player.stats,
    "explore": Player.explore,
    "run": Player.run,
    "fight": Player.fight,
    "suicide": Player.kill,
    "rest": Player.rest
}

#the input for the players chosen name and the title screen
print("")
name = input("Enter username... \n >> ")
hero = Player(name)

#prints the welcome screen
print(" ")
print("     █░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█ ")
print("     ▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█ ")
print(" ")
print("▄▀█ █▄▄ █▄█ █▀ █▀ ▄▀█ █░░   █▀▄ █▀▀ █▀ █▀▀ █▀▀ █▄░█ ▀█▀")
print("█▀█ █▄█ ░█░ ▄█ ▄█ █▀█ █▄▄   █▄▀ ██▄ ▄█ █▄▄ ██▄ █░▀█ ░█░")
print(" ")

while True:
    dif = input("Choose a difficulty: \n >> Easy (1) \n >> Normal (2) \n >> Hard (3)\n >> ")

    if dif == "1":
        print("You chose easy")
        hero.health += 20
        break
    elif dif == "2":
        print("You chose normal")
        hero.health += 10
        break
    elif dif == "3":
        print("You chose hard")
        hero.health += 0
        break
    else:
        print("Please choose one of the options")


print("\nTip: type help to bring up an actions menu. \n")

#the player must type enter for the game to start
while True:
    start = input("Type enter to start \n >> ")
    if start == "enter":
        break
print(" ")

#the monsters name and health stats
kraken_spawn = Monster("Kraken Spawn", 3)
cursed_diver = Monster("Cursed Diver", 10)
chasm_crawler = Monster("Chasm Crawler", 10)
#
#
#
#
#
#
kraken = Monster("Kraken", 150)

#the list of monsters
monsters = []

#adding the monsters to the list
monsters.append(kraken_spawn)
monsters.append(cursed_diver)
monsters.append(chasm_crawler)
monsters.append(kraken)

monster = monsters[0]


#prints the opening message to the game
print(f"{hero.name} touchs town on the sea floor, their torchlight shining through the dust and silt into the mouth of a dark cave...")

#the while loop that will get an input for the game to continue
while hero.health > 0 and kraken.health > 0:
    while hero.rest_count == 0:
        rest_now = input("*You need rest now* \n >> ")
        if rest_now == "rest":
            hero.rest(monster)
            break
    if hero.rest_count > 0:
        line = input("What do you want to do? \n >> ")
        if line in Commands.keys():
            Commands[line] (hero, monster)
        else:
            print(hero.name, "does not understand this suggestion")
        hero.rest_count -= 1

if hero.health > 0:
    print("You Won! Game Over.")
    credits()
else:
    print("You Lost! Game Over.")
    credits()
