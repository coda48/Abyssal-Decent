#Abyssal Descent by Joss

#import the random choice for the game
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
    def hurt(self, modifer=0):
        self.health = self.health - 0 - modifer
    #the function for the heal system
    def heal(self):
        self.health = self.health + randint(0,2)

#The class for the player
class Player(LivingThing):
    def __init__(self, name): 
        self.name = name
        self.health = 10
        self.rest_count = 10
        self.status = "normal"
        self.xp_points = 0
        self.xp_level = 0
        self.new_level = 10
        self.armor = ""
        self.weapon = ""
        self.invis_count = 0
        
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
        print(f">> XP level: {self.xp_level} <<")
        print(f">> Progress to next level {self.xp_points}/{self.new_level}")

    #the function that moves you from around
    def explore(self, monster):
        if randint(0,2) == 1:
            #if the current monster has the name of a monster in the list, print a special message about the monster for the story
            print (monster.flavour)
                #makes the status of the players confronted so it can fight
            self.status = "confronted"
        else:
            #the heal fucntion for exploring and finding no monsters
            self.heal()
            print("Your health is now", self.health)

    #the function to run away from a fight
    def run(self, monster):
        #to check if the player is in a fight
        if self.status == "Confonted":
            #makes the players no longer in a fight
            self.status = "normal"
            #regens the monsters health to full
            if monster.name == "Kraken Spawn":
                monster.health = 5
            elif monster.name == "Cursed Dive":
                monster.health = 10
            elif monster.name == "Chasm Crawler":
                monster.health = 10
            elif monster.name == "Kraken":
                monster.health = 50
            print(f"You ran away from {monster.name}")
        else:
            #if the player wasnt in a fight
            print("You cannon run if your not in a fight!")

    #the function that allows you to fight monsters in the game
    def fight(self, monster):
        #allows the currentmonster var to be accesed anywhere
        global currentmonster

        if self.status == "invisible":
            print('You are invisible, the monsters cannot see you')
            if self.weapon == "":
                monster.hurt(randint(1,3))
            if monster.health > 0:
                print(f"{monster.name} survived the attack")
                print(f"The monsters health is now: {monster.health}")
            # if you killed the monster
            else:
                print("Victory! You defeated", monster.name)
                currentmonster = monsters.pop(0)
                self.status = "normal"
                self.xp_points += monster.xp

                while self.xp_points >= self.new_level:
                    self.xp_level += 1
                    self.new_level *= 2
                    print("You leveled up!")
    
            self.invis_count -= 1
            if self.invis_count <= 0:
                self.status == "regular"
                #regens the monsters health to full
                if monster.name == "Kraken Spawn":
                    monster.health = 5
                elif monster.name == "Cursed Diver":
                    monster.health = 10
                elif monster.name == "Chasm Crawler":
                    monster.health = 10
                elif monster.name == "Kraken":
                    monster.health = 50
                print("Your invisibility ran out. You retreated from your current fight")
            else:
                pass

        #checks if the players is confronted by a monster
        elif self.status == "confronted": 
            #the damage dealing machinic in the fight
            self.hurt(monster.damage)
            #if you don't have a weapon make its so you do 1 to 3 damage
            if self.weapon == "":
                monster.hurt(randint(1,3))
            else:
                pass
            print(monster.name, "attacks you")
            #checks if the monster killed you
            if self.health <= 0:
                print("You were killed by", monster.name)
            #checks if neither you or the monster were killed
            elif monster.health > 0:
                print("You survied the attack from", monster.name)
                print("Your health is now:", self.health)
                print(f"The monsters health is now: {monster.health}")
            # if you killed the monster
            else:
                print("Victory! You defeated", monster.name)
                currentmonster = monsters.pop(0)
                self.status = "normal"
                self.xp_points += monster.xp

                while self.xp_points >= self.new_level:
                    self.xp_level += 1
                    self.new_level *= 2
                    print("You leveled up!")
                if monster.name == "Kraken Spawn":
                    if 1 == 1:
                        print("You found a Invisibility Potion")
                        item_list.append(invisibility_potion)

        else:
            #if you are not confronted by a monster
            print("You are safe for now, no need to fight")

    #the kill function made for testing
    def kill(self, monster):
        self.health = 0
        print(f"{hero.name} committed suicide")

    #the rest system for when you get tired
    def rest(self, monster):
        #resets the players rest counter to 10 if they are in need of rest
        if self.rest_count == 0:
            self.rest_count = 10
            print("You have rested, you now have full stamina points")
        else:
            #if they dont need rest
            print("You do not need to rest right now")
    
    def potion_use(invisibility_potion):
            if invisibility_potion in item_list:
                hero.invis_count = randint(3, 5)
                print(f"You are now invisable for {hero.invis_count} turns")
                item_list.pop(invisibility_potion)
            else:
                print("You dont have any Invisibility Potions")

#class for all monsters
class Monster(LivingThing):
    def __init__(self, name, health, xp, damage, flavour):
        self.name = name
        self.health = health
        self.xp = xp
        self.damage = damage
        self.flavour = flavour

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
class Weapon(Item):
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage

class Armor(Item):
    def __init__(self, name, buffer, description):
        self.name = name
        self.buffer = buffer
        self.description = description

class Potion(Item):
    def __init__(self, name, flavour, effect):
        self.name = name
        self.flavour = flavour
        self.effect = effect

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
    "rest": Player.rest,
    "use": Player.potion_use
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
    #if the dif (difficulty) is set to 1, to what is listed under 1. Same for 2 and 3
    if dif == "1":
        print(f"\nYour name is: {hero.name} \nYour difficulty: Easy\nYour Health: {hero.health}\n")
        #adds more health 
        hero.health += 20
        break
    elif dif == "2":
        print(f"\nYour name is: {hero.name} \nYour difficulty: Normal\nYour Health: {hero.health}\n")
        hero.health += 10
        break
    elif dif == "3":
        print(f"\nYour name is: {hero.name} \nYour difficulty: Hard\nYour Health: {hero.health}\n")
        hero.health += 0
        break
    else:
        #if they didnt chose a difficulty
        print("Please chose on of the options")

#the player must type enter for the game to start
while True:
    start = input("Type enter to start \n >> ")
    if start == "enter":
        break
print(" ")

print("\nTip: type help to bring up an actions menu. \n")

#the monsters name, health, damage, xp, and flavour
kraken_spawn = Monster(
    "Kraken Spawn",
    5,
    randint(1, 3),
    randint(1, 2),
    "While you are exploring around the entance of the cave, out of the shadowy crevices rushs what seems to be a singluar tentacle... the Kranken Spawn (type fight to fight the Kranken Spawn)"
)

cursed_diver = Monster(
    "Cursed Diver",
    10,
    randint(6, 8),
    randint(0, 5),
    "As you swim through the underwater depths of the ruinged caves, you being to find more and more interesting tressures, a golden crown here, a silver goblet there. As you are inspecting one of these objects, from out of the darkness ahead of you rises a diver like yourself... (type fight to fight the Cursed Diver)"
    )
chasm_crawler = Monster(
    "Chasm Crawler",
    10,
    randint(12, 15),
    randint(9, 15),
    "The decent further down the cave has led you to a tall, wide opening that even your touch light cannot reach the sides of. As you begin to slowly swim through the dark abyss arms and claws stast to grab at you, you slap them off and out of the darkness limps the Chasm Crawler... (type fight to fight the Chasm Crawler)"
    )

kraken = Monster(
    "Kraken",
    150,
    0,
    randint(30, 40), 
    "As you reach the end of the dark tunnel, your torch lights up the back wall of a huge caven. As you begin to look around, a giant tentacle slaps down next to you. Then from the darkness climbs the king of the ocean, The Kraken..."
    )

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

#the weapons list
weapons = []

#the weapons name, flavour, and damage
tentacle_sword = Weapon(
    "Tentacle Sword",
    "Dropped when the Kraken Spawn is killed, deal 1 to 3 damage",
    randint(1,3)
)

rusted_sword = Weapon(
    "Rusted Sword",
    "May be dropped when you kill the Cursed Driver, deals 2 to five damage",
    randint(2,5)
)

crawler_claw = Weapon(
    "Crawler Claw",
    "The weapon that you can be dropped from the monster Chasm Crawler, does 7 to 12 damages",
    randint(7,12)
)

trident = Weapon(
    "Trident",
    "The golden trident that summons lightning, does 20 to 30 damage",
    randint(20,30)
)

#add the weapons to the list
weapons.append(tentacle_sword)
weapons.append(rusted_sword)
weapons.append(crawler_claw)
weapons.append(trident)

#choosing a weapon
current_weapon = choice(weapons)

#removing the old weapon to the list
current_weapon = weapons.pop

item_list = []

invisibility_potion = Potion(
    "Invisibility Potion",
    "This potion will grand you invisibility for a limited amout of time",
    randint(3,5)
)

#the explore count for the story dialog. each time you explore it adds one to this count
explore_count = 0

#prints the opening message to the game
print(f"{hero.name} touchs down on the sea floor, their torchlight shining through the dust and silt into the mouth of a dark cave...")

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
                print("As you continue down futher into the dark cave, the cretures begin to become more restless, wary of the intruder in their home")
            elif explore_count == 15:
                print("The cave is slowy beginging to close up and narrow again, now you can see the walls of the tunnel with your torch")

        elif line == "fight":
            hero.rest_count -= 1
        elif line == "retreat":
            hero.rest_count -= 1

print("You Lost! Game Over.")
credits()
