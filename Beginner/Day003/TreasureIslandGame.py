print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\' . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Can you successfully navigate the island")
print("      and find the hidden treasure?")
print()
direction = input("Before you lies a fork in the road. Do you venture Left or Right? ")
if direction.upper() == "LEFT":
    print("You venture forth, travelling down the left fork in the road.")
    print("Ahead you see a lake with a large island in the middle.")
    print("This is called 'Treasure Island' - could that be where the treasure is?")
    print()
    print("   __ /\\__")
    print("~~~\\____ / ~~~~~~")
    print("~  ~~~   ~.")
    water_crossing = input("There is a dock with a boat tied up. Do you take the Boat, or Swim? ")
    if water_crossing.upper() == "BOAT":
        print("The boat successfully ferries you across the lake to...")
        print()
        print("                'TREASURE ISLAND'")
        print()
        print("*seriously, you should have seen that coming")
        print()
        print("You have made it safely to the treasure room. Before you are three doors.")
        print("                          Red, Yellow, Blue")
        door = input("Which do you open? ")
        if door.upper() == "YELLOW":
            print("Congratulations! You have found the Treasure!")
        elif door.upper() == "RED":
            print("WHY WOULD YOU OPEN THE DOOR THAT IS THE COLOR OF THE DEADLY DRAGON?")
            print("              _,-'/-'/")
            print("  .      __,-; ,'( '/")
            print("   \\.    `-.__`-._`:_,-._       _ , . ``")
            print("    `:-._,------' ` _,`--` -: `_ , ` ,' :")
            print("       `---..__,,--'            ` -'. -'")
            print()
            print("Game Over!")
        elif door.upper() == "BLUE":
            print("You open the blue door, and water rushes into the antechamber, filling it.")
            print("                             You drown")
            print("Game Over!")
        else:
            print("You can't follow directions")
            print("Game Over!")
    else:
        print("Giant crayfish grab at your ankles, dragging you down to the depths of the lake")
        print("where you find...")
        print("...you can't breath under water.")
        print("Game Over!")
else:
    print("Poor life choices befall you early. You have fallen down a hole.")
    print("Game Over!")

