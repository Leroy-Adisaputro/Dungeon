import random 

luck = 0
hp = 0
might = 0
dfs = 0
gold = 0
hit = 0
rmsc = 0
rmsl = 0
dg = 0
kr = random.randint(2,3)

def roller():
    roll = random.randint(1,14)
    global rmsc
    if roll == 1:
        print("This room is safe, continue on!")
    elif roll == 2:
        print("A treasure chest has been found!")
        open = input("Loot it? yes // no\n")
        if open.lower() == "yes":
            chestroll()
        else:
            print("You foolishly leave behind loot...")
            rmsc = rmsc + 1
    elif roll == 3:
        print("Here is the shop!")
        shoproll()
    elif roll >= 4:
        pveroll()
    else:
        print("Error: RE")

def shoproll():
    global rmsc
    global dfs
    global might
    global gold
    global hp
    rng = random.randint(1, 4)
    print("The shop can sell anything you find in this dungeon.")
    if rng == 1:
        action = input("The shop is selling a sword! Would you like to buy? Price: 2 Gold yes // no\n")
        if action.lower() == "yes":
            if gold >= 2:
                print("You buy the sword! your strength increases")
                might = might + 2
                gold = gold - 2
                rmsc = rmsc + 1
            elif gold <= 2:
                print("Insufficient funds")
                rmsc = rmsc + 1
        elif action.lower() == "no": 
            print("You leave the shop!")
            rmsc = rmsc + 1
    elif rng == 2:
        action = input("The shop is selling a sheild! Would you like to buy? Price: 2 Gold yes // no\n")
        if action.lower() == "yes":
            if gold >= 2:
                print("You buy the sheild! your defence increases")
                dfs = dfs + 2
                rmsc = rmsc + 1
                gold = gold - 2
            elif gold <= 2:
                print("Insufficient funds")
                rmsc = rmsc + 1
        else: 
            print("You leave the shop!")
            rmsc = rmsc + 1
    elif rng == 3:
        action = input("The shop is selling an instaheal! Would you like to buy? Price: 4 Gold yes // no\n")
        if action.lower() == "yes":
            if gold >= 4:
                print("You buy the heal! your health is recovered")
                hp = hp + 5
                rmsc = rmsc + 1
                gold = gold - 4
            elif gold <= 4:
                print("Insufficient funds")
                rmsc = rmsc + 1
        else: 
            print("You leave the shop!")
            rmsc = rmsc + 1
    elif rng == 4:
        action = input("The shop is selling a map! Would you like to buy? Price: 2 Gold yes // no\n")
        if action.lower() == "yes":
            if gold >= 2:
                rmsl = kr - rmsc
                print("You found a map. It says that to get to the starlight core you must clear", (kr), "rooms")
                print("Only", (rmsl), "rooms left")
                rmsc = rmsc + 1
                gold = gold - 2
            elif gold <= 2:
                print("Insufficient funds")
                rmsc = rmsc + 1
        else: 
            print("You leave the shop!")
            rmsc = rmsc + 1
    else:
        print("Error SRE")

def goldroll():
    global gold
    val = random.randint(1, 100)
    if val <= 32:
        gold = gold + 1
        print("You got 1 gold!")
    else:
        print("You got no gold!")

def pveroll():
    global rmsc
    global hp
    mobspawn = random.randrange(1,8)
    monster = mobspawn
    print("You have encountered", (mobspawn), "monsters!")
    while monster != 0:
        action = input("What do you do? attack // run\n")
        if action.lower() == "attack":
            val = random.randint(1,60)
            mstrhp = 100
            if  luck > val < might:
                print("You hit a critical strike! The monster dies imediately!")
                monster -= 1
                print("There are still", (monster), "monsters left")
                goldroll()
            elif  luck < val < might:
                hit = random.randint(might, 100)
                mstrhp -= hit
                print("You dealt", (hit), "damage")
                print("Monster health left:", (mstrhp))
                if mstrhp <= 0:
                    print("You killed a monster!")
                    monster -= 1
                    print("There are still", (monster), "monsters left")
                    goldroll()
            elif luck < val > might:
                print("You missed! The monster is counter-attacking you!")
                p_dmg = random.randint(10, 20)
                p_dmg -= dfs
                hp = hp - p_dmg
                if p_dmg <= 0:
                    print("You dodged it's attack!")
                elif p_dmg != 0:
                    print("You take", (p_dmg), "damage")
            else:
                print("Error: DRE")
        elif action.lower() == "run":
            print("You ran away from the monsters!")
            break
        else:
            print("Error: Unidentified action")

    if monster == 0:
        print("You have defeated all the monsters here!")
        rmsc = rmsc + 1

def lootroll():
    global rmsc
    global kr
    global rmsl
    val = random.randint(1,4)
    if val == 1:
        print("A green aura surrounds you, it engulfs you... you got healed!")
        hp == hp + 1 
        rmsc = rmsc + 1
    elif val == 2:
        print("You found a sword! You become stronger")
        might == might + 1
        rmsc = rmsc + 1
    elif val == 3:
        print("You found a sheild! You become tougher")
        dfs == dfs + 1
        rmsc = rmsc + 1
    elif val == 4:
        rmsl = kr - rmsc
        print("You found a map. It says that to get to the starlight core you must clear", (kr), "rooms")
        print("Only", (rmsl), "rooms left")
        rmsc = rmsc + 1
    else:
        print("Error: LRE")

def chestmobroll():
    global dg
    val = random.randint(1,2)
    if val == 1:
        print("You rummaged through the chest and found nothing...unlucky")
    elif val == 2:
        print("A monster was hiding in the chest!")
        print("Monsters in the chest are weak and cannot attack")
        while dg >= 3:
            action = input("What do you do? attack // run\n")
            if action.lower() == "attack":
                dg = random.randint(1,5)
                if dg <= 3:
                    print("You killed the monster!")
                    goldroll()
                elif dg >= 3:
                    print("You missed! The monster is unable to counter-attack!")
            else:
                print("You run away!")
    else:
        print("Error: CMRE")

def chestroll():
    global rmsc
    roll = random.randint(1,20)
    if roll <= luck:
        print("You've found some loot!")
        lootroll()
    elif roll >= luck:
        chestmobroll()
        rmsc = rmsc + 1
    else:
        print("Error: CRE")

key = input("Start? yes // no\n")
if key.lower() == "yes":
    while luck == 0:
        diff = input("Select difficulty? Easy // Medium // Hard\n")
        diff = diff.lower()
        if diff.lower() == "easy":
            hp = 30
            luck = 15
            might = 40
            dfs = 10
            print("Health =", (hp), "Luck =", (luck), "Strength =", (might), "Defence =", (dfs))
            print("Type help for more info")
            print("You enter a cellar underneath a wrecked house. The snarls of monsters could be heard echoing throughout the dark underground. Its a goblin's den.\n You venture on deeper only to realize it was a maze with endless turns. But you can't turn back now...\n The walls have runes inscribed in them they read: There is a room of starlight hidden in this maze, inside it you will find a core, find it and be set free.\n Here, you can infinitely grow")
        elif diff.lower() == "medium":
            hp = 20
            luck = 10
            might = 30
            dfs = 10
            print("Health =", (hp), "Luck =", (luck), "Strength =", (might), "Defence =", (dfs))
            print("Type help for more info")
            print("You enter a cellar underneath a wrecked house. The snarls of monsters could be heard echoing throughout the dark underground. Its a goblin's den.\n You venture on deeper only to realize it was a maze with endless turns. But you can't turn back now...\n The walls have runes inscribed in them they read: There is a room of starlight hidden in this maze, inside it you will find a core, find it and be set free.\n Here, you can infinitely grow")
        elif diff.lower() == "hard":
            hp = 15
            luck = 5
            might = 20
            dfs = 5
            print("Health =", (hp), "Luck =", (luck), "Strength =", (might), "Defence =", (dfs))
            print("Type help for more info")
            print("You enter a cellar underneath a wrecked house. The snarls of monsters could be heard echoing throughout the dark underground. Its a goblin's den.\n You venture on deeper only to realize it was a maze with endless turns. But you can't turn back now...\n The walls have runes inscribed in them they read: There is a room of starlight hidden in this maze, inside it you will find a core, find it and be set free.\n Here, you can infinitely grow")
        else:
           print("That is not a difficulty\nPlease type in easy, medium or hard")
else:
    print("Ending simulation")
    exit()

while rmsc != kr:
    key = input("would you like to move left or right?\n")
    print("You have cleared", (rmsc), "rooms, find the starlight core.")
    if key.lower() == "left":
        roller()
    elif key.lower() =="right":
        roller()
    elif key.lower() == "inventory":
        print("You have ", (gold), "gold")
    elif key.lower() == "stats":
        print("Health =", (hp), "Luck =", (luck), "Strength =", (might), "Defence =", (dfs))
    elif key.lower() == "help":
        print("Use help(action // misc)")
    elif key.lower() == "help action":
        print("Type left or right to move")
        print("Type attack to attack")
        print("Type buy to buy in the shop")
        print("Type loot to loot a chest")
    elif key.lower() == "help misc":
        print("Type stats to check stats menu")
        print("Type inventory to check gold")
    else:
        print("You can't do that right now.")

    if hp == 0:
        print("Game over! You died!")
        print("End of simulation!")
