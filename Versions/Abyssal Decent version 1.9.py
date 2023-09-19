# Abyssal Descent by Joss

# import the random choice for the game
from random import randint, choice

# The class for all living things
class LivingThing():
    # the function for the base living thing
    def __init__(self):
        self.name = " "
        self.health = 1
    
    #the hurt function
    def hurt(self, modifer=0, strength=0):
        self.health = self.health - 0 - modifer - strength
    # the function for the heal system

    def heal(self):
        self.health = self.health + randint(0, 2)

# The class for the player
class Player(LivingThing):
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.full_health = 10
        self.rest_count = 10
        self.status = "normal"
        self.xp_points = 0
        self.xp_level = 0
        self.new_level = 10
        self.armor = ""
        self.weapon = ""
        self.invis_count = 0
        self.strength_count = 0
        self.potion_effect = "none"
        self.weapon_find = "seaching"

    # the functions for the commands
    def help(self, monster, strength_potion, invisibility_potion, health_potion):
        print(">> Help <<: Brings up the action menu")
        print(">> Stats <<: brings up your stats")
        print(">> Explore <<: allows you to explore the world")
        print(">> Retreat <<: Allows you to retreat from fights")
        print(">> Fight <<: Allows you to fight monsters")
        print(">> Rest <<: Will refill you stamina points to full")

    # the function that displays your player stats
    def stats(self, monster, strength_potion, invisibility_potion, health_potion):
        print(f">> Name: {self.name}")
        print(f">> Health: {self.health}")
        print(f">> Status: {self.status}")
        print(f">> Stamina points: {self.rest_count}")
        print(f">> XP level: {self.xp_level}")
        print(f">> Progress to next level: {self.xp_points}/{self.new_level}")
        print(f">> Current Weapon: {self.weapon}")

    # the function that moves you from around
    def explore(self, monster, strength_potion, invisibility_potion, health_potion):
        #allows to edit ouside of scope
        global current_weapon

        if randint(0, 2) == 1:
            # if the current monster has the name of a monster in the list, print a special message about the monster for the story
            print(monster.flavour)
            # makes the status of the players confronted so it can fight
            self.status = "confronted"

        else:
            if randint(1, 2) == 1:
                # the heal fucntion for exploring and finding no monsters
                self.heal()
                print("Your health is now", self.health)
            if randint(0,2) == 1:
                print(f"You found {weapon.name}.")
                while True:
                    i = input("Type equip to equip weapon, or ignore to leave weapon \n >> ")
                    if i == "equip":
                        if self.weapon_find != "found":
                            print(f"You equipped {weapon.name} (type drop to remove weapon)")
                            self.weapon = weapon.name
                            self.weapon_find = "found"
                            current_weapon = weapons.pop(0)
                            break
                        elif self.weapon_find != "seaching":
                            print("You already have a weapon equipped, type drop to remove that weapon")
                            break
                    elif i == "ignore":
                        print('You igored the weapon')
                        self.weapon_find = "seaching"
                        current_weapon = weapons.pop(0)
                        break
                    if i != "equip" or "igore":
                        print("Please type either equip or ignore")
        
    def drop(self, monster, strength_potion, invisibility_potion, health_potion):
        global current_weapon
        print(f"You dropped {weapon.name}")
        self.weapon = ""
        current_weapon = weapons.pop(0)
        self.weapon_find = "searching"
        

    def pots(self, monster, strength_potion, invisibility_potion, health_potion):
        if randint(1, 3) == 1:
            item_list.append(invisibility_potion)
            print("you picked up an invisibility_potion")
        if randint(1, 4) == 1:
            item_list.append(strength_potion)
            print("You picker up a strength potion")
        if randint(1, 2) == 1:
            item_list.append(health_potion)
            print("you picked up a health potion")

    # the function to run away from a fight
    def run(self, monster, strength_potion, invisibility_potion, health_potion):
        # to check if the player is in a fight
        if self.status == "confronted":
            # makes the players no longer in a fight
            self.status = "normal"
            # regens the monsters health to full
            monster.health = monster.max_health
            print(f"You ran away from {monster.name}")
        else:
            # if the player wasnt in a fight
            print("You cannon run if your not in a fight!")

    # the function that allows you to fight monsters in the game
    def fight(self, monster, strength_potion, invisibility_potion, health_potion):
        # allows the currentmonster var to be accesed anywhere
        global currentmonster

        # checks if the players is confronted by a monster
        if self.status == "confronted":
            # the damage dealing machinic in the fight
                self.hurt(monster.damage)
            # if you don't have a weapon make its so you do 1 to 3 damage
                if self.weapon == "":
                    monster.hurt(randint(1, 3))
                else:
                    monster.hurt(weapon.damage)
                # if you have a strength potion
                    if self.potion_effect == "strength":
                        monster.hurt(strength_potion.damage)
                        self.strength_count -= 1

                print(monster.name, "attacks you")
            # checks if the monster killed you
                if self.health <= 0:
                    print("You were killed by", monster.name)
            # checks if neither you or the monster were killed
                elif monster.health > 0:
                    print("You survied the attack from", monster.name)
                    print("Your health is now:", self.health)
                    print(f"The monsters health is now: {monster.health}")
            # if you killed the monster
                else:
                    print("Victory! You defeated", monster.name)
                # removes the monster from the list after it is killed
                    currentmonster = monsters.pop(0)
                    self.status = "normal"
                # adds the monsts xp drop to your xp points
                    self.xp_points += monster.xp

                # if your xp is above the level amount, level up
                    while self.xp_points >= self.new_level:
                        self.xp_level += 1
                        self.new_level *= 2
                        print("You leveled up!")
                # drops a potion from a monsters
                    self.pots(monster, strength_potion, invisibility_potion, health_potion)

        else:
            # if you are not confronted by a monster
            print("You are safe for now, no need to fight")

    # the kill function made for testing
    def kill(self, monster, strength_potion, invisibility_potion, health_potion):
        self.health = 0
        print(f"{hero.name} committed suicide")

    # the rest system for when you get tired
    def rest(self, monster, strength_potion, invisibility_potion, health_potion):
        # resets the players rest counter to 10 if they are in need of rest
        if self.rest_count == 0:
            self.rest_count = 10
            print("You have rested, you now have full stamina points")
        else:
            # if they dont need rest
            print("You do not need to rest right now")

    # the fucntion for using potions
    def use(self, monster, strength_potion, invisibility_potion, health_potion):
        while True:
            # i is the varible for the input
            i = input("Type what potion you would like to use? \n >> ")
            # checks what potion that want to use
            if i == "invisibility potion":
                # checks if the potion is in the item list
                if invisibility_potion in item_list:
                    # sets the effect status to the potion effect
                    self.potion_effect = "invisible"
                    # adds to the invisibilty count
                    self.invis_count = randint(3, 5)
                    print(
                        f"You are now invisable for {self.invis_count} turns")
                    # removes the potion from the players inventory
                    item_list.remove(invisibility_potion)
                    # stops the loop
                    break
                else:
                    # if you dont own an Invisibility Potions
                    print("You dont have any Invisibility Potions")
            # checks for different potion name
            elif i == "strength potion":
                if strength_potion in item_list:
                    self.strength_count = randint(3, 4)
                    self.potion_effect = "strength"
                    print(
                        f"You used a {i} potion, you now have strength for {self.strength_count} turns")
                    item_list.remove(strength_potion)
                    break
            elif i == "health potion":
                self.health = self.full_health
                print(
                    f"You used a health potion, your health is now {self.health}")
                item_list.remove(health_potion)
                break

# class for all monsters
class Monster(LivingThing):
    def __init__(self, name, health, xp, damage, max_health, flavour):
        self.name = name
        self.health = health
        self.xp = xp
        self.damage = damage
        self.max_health = max_health
        self.flavour = flavour

# the base class for items, potions, weapons, and armor
class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

# the class for weapons
class Weapon(Item):
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage

# the class for armor
class Armor(Item):
    def __init__(self, name, buffer, description):
        self.name = name
        self.buffer = buffer
        self.description = description

# the class for potions
class Potion(Item):
    def __init__(self, name, flavour, damage):
        self.name = name
        self.flavour = flavour
        self.damage = damage

# the credits for when the game ends
def credits():
    print(" ")
    print("▀█▀ █░█ ▄▀█ █▄░█ █▄▀ █▀   █▀▀ █▀█ █▀█   █▀█ █░░ ▄▀█ █▄█ █ █▄░█ █▀▀")
    print("░█░ █▀█ █▀█ █░▀█ █░█ ▄█   █▀░ █▄█ █▀▄   █▀▀ █▄▄ █▀█ ░█░ █ █░▀█ █▄█")
    print(" ")


# The list for all the commands
Commands = {
    "help": Player.help,
    "stats": Player.stats,
    "explore": Player.explore,
    "retreat": Player.run,
    "fight": Player.fight,
    "suicide": Player.kill,
    "rest": Player.rest,
    "use": Player.use,
    "drop":Player.drop
}

# the input for the players chosen name and the title screen
print("")
name = input("Enter username... \n >> ")
hero = Player(name)

# prints the welcome screen
print(" ")
print("     █░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█ ")
print("     ▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█ ")
print(" ")
print("▄▀█ █▄▄ █▄█ █▀ █▀ ▄▀█ █░░   █▀▄ █▀▀ █▀ █▀▀ █▀▀ █▄░█ ▀█▀")
print("█▀█ █▄█ ░█░ ▄█ ▄█ █▀█ █▄▄   █▄▀ ██▄ ▄█ █▄▄ ██▄ █░▀█ ░█░")
print(" ")

# the while loop that makes it so the player must choose a difficulty.
while True:
    dif = input(
        "Choose a difficulty: \n >> Easy (1) \n >> Normal (2) \n >> Hard (3)\n >> ")
    # if the dif (difficulty) is set to 1, to what is listed under 1. Same for 2 and 3
    if dif == "1":
        # adds more health
        hero.health += 20
        hero.full_health += 20
        print(
            f"\nYour name is: {hero.name} \nYour difficulty: Easy\nYour Health: {hero.health}\n")
        break
    elif dif == "2":
        hero.health += 10
        hero.full_health += 10
        print(
            f"\nYour name is: {hero.name} \nYour difficulty: Normal\nYour Health: {hero.health}\n")
        break
    elif dif == "3":
        print(
            f"\nYour name is: {hero.name} \nYour difficulty: Hard\nYour Health: {hero.health}\n")
        break
    else:
        # if they didnt chose a difficulty
        print("Please chose on of the options")

# the player must type enter for the game to start
while True:
    start = input("Type enter to start\n >> ")
    if start == "enter":
        break
print(" ")

print("\nTip: type help to bring up an actions menu. \n")

# the monsters name, health, damage, xp, and flavour
kraken_spawn = Monster(
    "Kraken Spawn",
    5,
    randint(1, 3),
    randint(1, 2),
    5,
    "While you are exploring around the entrance of the cave, out of the shadowy crevices rushes what seems to be a singular tentacle... the Kraken Spawn (type fight to fight the Kraken Spawn)"
)

cursed_diver = Monster(
    "Cursed Diver",
    10,
    randint(6, 8),
    randint(0, 5),
    10,
    "As you swim through the underwater depths of the ruined caves, you begin to find more and more interesting treasures, a golden crown here, a silver goblet there. As you are inspecting one of these objects, from out of the darkness ahead of you rises a diver like yourself... (type fight to fight the Cursed Diver)"
)
chasm_crawler = Monster(
    "Chasm Crawler",
    10,
    randint(12, 15),
    randint(9, 15),
    10,
    "The descent further down the cave has led you to a tall, wide opening that even your touch light cannot reach the sides of. As you begin to slowly swim through the dark abyss, arms and claws start to grab at you, you slap them off and out of the darkness limps the Chasm Crawler... (type fight to fight the Chasm Crawler)"
)

glowing_jellyfish = Monster(
    "Glowing Jellyfish",
    8,
    randint(1, 2),
    2,
    8,
    "The depths reveal a mesmerizing display of Glowing Jellyfish. Beware their stinging tentacles (type fight to engage)."
)

shadowy_serpent = Monster(
    "Shadowy Serpent",
    12,
    randint(6, 8),
    4,
    12,
    "You feel a sudden chill as the Shadowy Serpent slithers closer, ready to ambush (type fight to confront the Serpent)."
)

cursed_seaweed = Monster(
    "Cursed Seaweed",
    15,
    randint(7, 9),
    3,
    15,
    "A sinister tangle of Cursed Seaweed rises from the ocean floor, seeking its next prey (type fight to face the Seaweed)."
)

merman_raider = Monster(
    "Merman Raider",
    20,
    randint(9, 12),
    6,
    20,
    "You encounter a hostile Merman Raider, armed with a menacing trident (type fight to battle the Raider)."
)

skeletal_mariner = Monster(
    "Skeletal Mariner",
    25,
    randint(12, 15),
    7,
    25,
    "The ghostly visage of a Skeletal Mariner materializes before you, brandishing a rusty cutlass (type fight to confront the Mariner)."
)

abyssal_guardian = Monster(
    "Abyssal Guardian",
    30,
    randint(15, 20),
    10,
    30,
    "A massive, heavily armored Abyssal Guardian emerges from the depths, ready to defend its territory (type fight to challenge the Guardian)."
)

electric_eel = Monster(
    "Electric Eel",
    18,
    randint(8, 12),
    8,
    18,
    "An Electric Eel crackles with energy as it darts toward you, ready to shock its prey (type fight to face the Eel)."
)

lurking_leviathan = Monster(
    "Lurking Leviathan",
    50,
    randint(25, 30),
    15,
    50,
    "A colossal Lurking Leviathan rises from the abyssal depths, its presence sending shockwaves through the water (type fight to confront the Leviathan)."
)

giant_clam = Monster(
    "Giant Clam",
    15,
    randint(5, 8),
    5,
    15,
    "A Giant Clam opens wide, revealing rows of razor-sharp teeth within. It lunges forward to snap shut (type fight to battle the Clam)."
)

murky_octopus = Monster(
    "Murky Octopus",
    25,
    randint(10, 15),
    12,
    25,
    "A Murky Octopus with long, twisting tentacles approaches menacingly, ready to ensnare its prey (type fight to face the Octopus)."
)

kraken = Monster(
    "Kraken",
    150,
    0,
    randint(30, 40),
    150,
    "As you reach the end of the dark tunnel, your torch lights up the back wall of a huge cave. As you begin to look around, a giant tentacle slaps down next to you. Then from the darkness climbs the king of the ocean, The Kraken..."
)

# the list of monsters
monsters = []

# adding the monsters to the list
monsters.append(kraken_spawn)
monsters.append(cursed_diver)
monsters.append(chasm_crawler)
monsters.append(glowing_jellyfish)
monsters.append(shadowy_serpent)
monsters.append(cursed_seaweed)
monsters.append(merman_raider)
monsters.append(skeletal_mariner)
monsters.append(abyssal_guardian)
monsters.append(electric_eel)
monsters.append(lurking_leviathan)
monsters.append(giant_clam)
monsters.append(murky_octopus)
monsters.append(kraken)

# choosing the monster from the list
monster = choice(monsters)

# removes the monster from the list once chosen
currentmonster = monsters.pop(0)

# the weapons name, flavor, and damage
tentacle_sword = Weapon(
    "Tentacle Sword",
    "Dropped when the Kraken Spawn is killed, deal 1 to 3 damage",
    randint(1, 3)
)

rusted_sword = Weapon(
    "Rusted Sword",
    "May be dropped when you kill the Cursed Diver, deals 2 to five damage",
    randint(2, 5)
)

crawler_claw = Weapon(
    "Crawler Claw",
    "The weapon that you can be dropped from the monster Chasm Crawler, does 7 to 12 damages",
    randint(7, 12)
)

trident = Weapon(
    "Trident",
    "The golden trident that summons lightning, does 20 to 30 damage",
    randint(20, 30)
)

coral_dagger = Weapon(
    "Coral Dagger",
    "A sharp dagger crafted from razor-sharp coral fragments, deals 3 to 6 damage",
    randint(3, 6)
)

shark_tooth_spear = Weapon(
    "Shark Tooth Spear",
    "A menacing spear tipped with deadly shark teeth, deals 5 to 8 damage",
    randint(5, 8)
)

trident_of_the_abyss = Weapon(
    "Trident of the Abyss",
    "A mystical trident that harnesses the power of the abyss, deals 15 to 25 damage",
    randint(15, 25)
)

seaweed_whip = Weapon(
    "Seaweed Whip",
    "A flexible whip made of cursed seaweed, deals 8 to 12 damage",
    randint(8, 12)
)

barnacle_hammer = Weapon(
    "Barnacle Hammer",
    "A heavy hammer encrusted with sharp barnacles, deals 10 to 15 damage",
    randint(10, 15)
)

deep_sea_axe = Weapon(
    "Deep Sea Axe",
    "A formidable axe forged in the depths, deals 12 to 20 damage",
    randint(12, 20)
)

sirens_songblade = Weapon(
    "Siren's Songblade",
    "A beautiful but deadly sword enchanted with the haunting melody of sirens, deals 18 to 28 damage",
    randint(18, 28)
)

abyssal_blade = Weapon(
    "Abyssal Blade",
    "The ultimate weapon forged from the essence of the abyss, deals 30 to 40 damage",
    randint(30, 40)
)

# the weapons list
weapons = []

# add the weapons to the list
weapons.append(tentacle_sword)
weapons.append(rusted_sword)
weapons.append(crawler_claw)
weapons.append(trident)
weapons.append(coral_dagger)
weapons.append(shark_tooth_spear)
weapons.append(trident_of_the_abyss)
weapons.append(seaweed_whip)
weapons.append(barnacle_hammer)
weapons.append(deep_sea_axe)
weapons.append(sirens_songblade)
weapons.append(abyssal_blade)


# choosing a weapon
weapon = choice(weapons)

# removing the old weapon to the list
current_weapon = weapons.pop(0)

# the list for potions
item_list = []

# the potions, name, flavour
invisibility_potion = Potion(
    "Invisibility Potion",
    "This potion will grand you invisibility for a limited amout of time",
    0
)

strength_potion = Potion(
    "Strength Potion",
    "This potion add damage to your attack",
    0
)

health_potion = Potion(
    "Health Potion",
    "This potion will heal you back up to full health",
    randint(4,5)
)

# the explore count for the story dialog. each time you explore it adds one to this count
explore_count = 0

# prints the opening message to the game
print(f"{hero.name} touchs down on the sea floor, their torchlight shining through the dust and silt into the mouth of a dark cave...")

# the while loop that will get an input for the game to continue
while hero.health > 0 and kraken.health > 0:
    # if the rest count = 0, the player must rest
    while hero.rest_count == 0:
        rest_now = input(
            "*You are out of stamina points, you need rest now* \n >> ")
        # this calls the rest function to reset the players rest count
        if rest_now == "rest":
            hero.rest(monster, strength_potion, invisibility_potion, health_potion)
            break
    # this if checking if the command you entered is in the commands dictionary
    if hero.rest_count > 0:
        line = input("What do you want to do? \n >> ")
        if line in Commands.keys():
            Commands[line](hero, currentmonster, strength_potion, invisibility_potion, health_potion)
        else:
            # this will be printed if the command isn't in the command dictionary
            print(hero.name, "does not understand this suggestion")

        # if the command that is run is one of these, it will remove one of the players rest counters
        if line == "explore":
            hero.rest_count -= 1
            # adds 1 to the explore count each time you explore
            explore_count += 1
            # this is to add to the story of the game, by telling the player about their suroundings
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

# rolls the credits when you die
credits()
