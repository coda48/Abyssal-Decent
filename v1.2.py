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
        print(">> Fight <<: Allows you to fight monsters")
        print(">> Rest <<: Will refill you stamina points to full")
    
    #the function that displays your player stats
    def stats(self, monster):
        print(f">> Name: {self.name} <<")
        print(f">> Health: {self.health} <<")
        print(f">> Status: {self.status} <<")
        print(f">> Stamina points: {self.rest_count} <<")

    #the function that moves you from around
    def explore(self, monster):
        if randint(0,2) == 1:
            if monster.name == "Kraken Spawn":
                print("While you are exploring around the entance of the cave, out of the and rushes are single tenticle... the Kranken Spawn")
            elif monster.name == "Kraken":
                print("As you reach the end of the dark tunnel, your torch lights up the back wall of a huge caven. As you begin to look around, a giant tenticle slaps down next to you. Then from the darkness climbs the king of the ocean, The Kraken...")
            self.status = "confronted"
        else:
            self.regen()
            print("Your health is now", self.health)

    #the function to run away from a fight
    def run(self, monster):
        if self.status == "Confonted":
            self.status = "normal"
            if monster.name == "Kraken Spawn":
                monster.health = 5
            elif monster.name == "Cursed Dive":
                monster.health = 10
            elif monster.name == "Chasm Crawler":
                monster.health = 10
            elif monster.name == "Kraken":
                monster.health = 150
            print(f"You ran away from {monster.name}")

    #the function that allows you to fight monsters in the game
    def fight(self, monster):
        global currentmonster
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
                currentmonster = monsters.pop(0)
                self.status = "normal"
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
            print("You have rested, you now have full stamina points")
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
    "retreat": Player.run,
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


#the while loop that makes it so the player must choose a difficulty.
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
        print("Please chose on of the options")

#the player must type enter for the game to start
while True:
    start = input("Type enter to start \n >> ")
    if start == "enter":
        break
print(" ")



print("\nTip: type help to bring up an actions menu. \n")


#the monsters name and health stats
kraken_spawn = Monster("Kraken Spawn", 5)
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

#choosing the monster from the list
monster = choice(monsters)

#removes the monster from the list once chosen
currentmonster = monsters.pop(0)

#this is the4 explore count for when to run game dialogs for the story
explore_count = 0

#prints the opening message to the game
print(f"{hero.name} touchs town on the sea floor, their torchlight shining through the dust and silt into the mouth of a dark cave...")

#the while loop that will get an input for the game to continue
while hero.health > 0 and kraken.health > 0:
    #if the rest count = 0, the player must rest
    while hero.rest_count == 0:
        rest_now = input("*You are out of stamina points, you need rest now* \n >> ")
        #this calls the rest function to reset the players rest count
        if rest_now == "rest":
            hero.rest(monster)
            break
    #this if checking if the command you entered is in the commands dictionary
    if hero.rest_count > 0:
        line = input("What do you want to do? \n >> ")
        if line in Commands.keys():
            Commands[line] (hero, currentmonster)
        else:
            #this will be printed if the command isn't in the command dictionary
            print(hero.name, "does not understand this suggestion")

        #if the command that is run is one of these, it will remove one of the players rest counters
        if line == "explore":
            hero.rest_count -= 1
            #adds 1 to the explore count each time you explore
            explore_count += 1
            #this is to add to the story of the game, by telling the player about their suroundings
            if explore_count < 2:
                print("As you explore the inside of the cave, creatures scuttle away from for the bright torch light into shadowy crevice in the dusty rocks. ")
            elif explore_count == 10:
                print("As you continue down futher inot the dark cave, the cretures begin to become more restless, wary of the visitor in their home")
            elif explore_count == 15:
                print("The creatues are becoming bolder and bigger. Soon they will begin to get hungry")

        elif line == "fight":
            hero.rest_count -= 1
        elif line == "retreat":
            hero.rest_count -= 1


if hero.health > 0:
    print("You Won! Game Over.")
    credits()
else:
    print("You Lost! Game Over.")
    credits()