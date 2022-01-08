import random



#create dictionaries to fill character stats?
#use input to make modifiers variables



#create D20

def RollAttack():
    profiency = int(input("Profiency #: "))
    modifier = int(input("Modifier, STR or DEX #: "))
    roll = int (random.randint(1,20))
    total = roll + modifier + profiency
    print("Rolled", roll)
    print("Total", total)

    if roll == 20:
        print("Natural 20!")

    elif roll == 1:
        print("Natural 1 :/")

#create Damage dice, D4,D6,D8,D12,D10

def RollDamage():
    faces = int(input("How many sides on a die? "))
    num_dice = int(input("How many dice? "))
    diceModifier = int(input("Modifier, STR or DEX #: "))

    rolls = []
    for die in range(num_dice):
        dice_roll = random.randint(1, faces)
        rolls.append(dice_roll)
        print("You rolled ", dice_roll)

        rolls_modified = [x+diceModifier for x in rolls]
        total = sum(rolls_modified)
        print("Total is ", total)
        



#then add modifier to each item in the list

#get the total of the list
    

#print("Rolls plus modifier ", rolls_modified)
    
