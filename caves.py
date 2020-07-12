import os
import random


def clear():
    """ Clear the screen
    """
    os.system("cls" if os.name == "nt" else "clear")


def show_player_status():
    """ Prints player status including, HP, level info, gold, number of caves 
        survived, and inventory.
    """
    clear()
    print("Player '{name}' Stats".format(name=name))
    print("HP: {health}/100".format(health=health))
    print("Lvl: {level} ({local_xp}/1000 xp)".format(level=xp // 1000, local_xp=xp % 1000))
    print("Gold:", gold)
    print("Caves survived:", caves_survived)
    print("\nYour inventory consists of these items:")

    # Print all items in inventory
    if inventory:
        for item in inventory:
            print("  * " + item)
    else:
        print("  ~nothing~")

    press_enter()


def press_enter():
    """ Prompts the player to press enter and waits for input.
    """
    input("\nPress enter to continue...")


def load_file(filename):
    """ Reads text file at `filename` and returns lines as a list.
    """
    with open(filename, 'r') as f:
        file_contents = f.read()
    
    output_list = list()
    # Split file into list of lines and iterate
    # through it
    for line in file_contents.splitlines():
        # Check if line, after being stripped, is not blank.
        if line.strip():
            # Toss it in the output list
            output_list.append(line.strip())
    # Hand the output back
    return output_list


# I moved these lines to below the function declarations
#  because they now rely on one of the functions we wrote.
ENEMY_OPTIONS = load_file("enemies.dat")
INJURY_OPTIONS = load_file("injuries.dat")
LOOT_OPTIONS = load_file("loot.dat")

clear()
print("Welcome to CAVES, young traveler.\n")

# Get player name
while True:
    name = input("Enter your name: ").strip().title()
    # Check if name is valid
    if name:
        break

# Initialize player stats
xp = 0
gold = 0
health = 100
inventory = list()
caves_survived = 0

while health > 0:
    show_player_status()
    correct_choice = random.choice(('left', 'right'))

    clear()
    print("\n  Ahead of you lies two caves.")
    print("  In one: great fortune and loot,")
    print("  but in the other lies death.\n")

    # Get cave choice
    while True:
        choice = input("Which cave do you choose? (left or right) ")
        # Clean user input
        choice = choice.lower().strip()
        # Check if choice is valid
        if choice in ('left', 'right'):
            # Exit loop
            break
        else:
            print("\nInvalid choice. (you must type either 'left' or 'right')")

    print("\n  You've selected the {choice} cave.".format(choice=choice))
    print("  You enter the cave, unsure of what awaits you...")
    press_enter()

    clear()

    if choice == correct_choice:
        print("\n  You chose wisely! You emerge from the cave unscathed")
        print("  and with new loot.")

        # Choose how many items the player will receive
        # (between 1 and 3)
        for i in range(random.randrange(1, 4)):
            # Give player a random item
            inventory.append(random.choice(LOOT_OPTIONS))

        # Give player between 0 and 100 gold
        gold += random.randrange(101)
        # Give player between 200 and 1500 xp
        xp += random.randrange(200, 1501)
    else:
        print("\n  Poor choice! You encounter great peril within"
              " that evil place.")
        # Choose a damage value between 1 and 99.
        # This prevents the player being killed in one hit.
        damage = random.randrange(1, 100)

        # Decide whether player is attacked by enemy or
        # harmed by other means.
        if random.randrange(2):
            enemy = random.choice(ENEMY_OPTIONS)
            # I split up "you" and "suffer ..." simply to keep
            # the line from getting to long, there's no real
            # technical reason for it.
            print("  In a run-in with a terrible", enemy, "you",
                "suffer", damage, "damage.")
        else:
            injury = random.choice(INJURY_OPTIONS)
            print("  You {injury} and suffer {damage} damage.".format(injury=injury,
                                                                      damage=damage))

        # Give player between 20 and 100 xp
        xp += random.randrange(20, 101)
        # Apply damage
        health -= damage

    if health > 0:
        caves_survived += 1
    press_enter()

clear()
print("YOU DIED. GAME OVER.")
print("Caves survived:", caves_survived)
press_enter()
