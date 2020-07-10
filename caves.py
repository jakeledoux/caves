import os
import random

ENEMY_OPTIONS = ['skeleton', 'bear', 'vampire', 'demon', 'dragon', 'Mezrah',
                 'ogre', 'man-eating spider', 'large squirrel']
LOOT_OPTIONS =  ['gilded sword', 'potion of long eyelashes', '$15 iTunes gift card',
                 'pip-boy', 'assassins creed wrist dagger', 'x-ray glasses',
                 'Half-Life 3', 'ET', 'rollerskates', 'a pompadour wig',
                 'wooden shield', 'the matrix sunglasses', 'desert eagle',
                 'metal shield', 'golden shield', 'diamond shield', 'wooden sword',
                 'bronze sword', 'silver sword', 'diamond sword', 'a wiimote',
                 'nintendo ds', 'indiana jones 4 on dvd', 'iphone 4',
                 'guns n roses poster', 'chain-mail armor', 'leather armor',
                 'nike sneakers', 'sneakers of high jumping', 'tapout backpack',
                 'tears for fears t-shirt', 'skyrim helmet', 'plastic bag helmet',
                 'g36 assault rifle', 'lightsaber']

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def show_player_status():
    # Print player status
    clear()
    print(f"Player '{name}' Stats")
    print(f"HP: {health}/100")
    print(f"Lvl: {xp // 1000} ({xp % 1000}/1000 xp)")
    print(f"Gold: {gold}")
    print(f"Caves survived: {caves_survived}")
    print(f"\nYour inventory consists of these items:")
    if inventory:
        for item in inventory:
            print("  * " + item)
    else:
        print("  *nothing*")

    press_enter()

def press_enter():
    input("\nPress enter to continue...")

clear()
print("Welcome to CAVES, young traveler.\n")

name = input("Enter your name: ").strip().title()

# Initialize player stats
xp = 0
gold = 0
health = 100
inventory = []
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

    print(f"\n  You've selected the {choice} cave.")
    print("  You enter the cave, unsure of what awaits you...")
    press_enter()

    clear()

    if choice == correct_choice:
        print("\n  You chose wisely! You emerge from the cave unscathed\n  and with new loot.")
        # Give player a random item
        inventory.append(random.choice(LOOT_OPTIONS))
        # Give player between 0 and 100 gold
        gold += random.randrange(101)
        # Give player between 200 and 1500 xp
        xp += random.randrange(200, 1501)
    else:
        print("\n  Poor choice! You encounter great peril within that evil place.")
        # Choose a damage value between 1 and 99. (Prevents 1-hit killing player)
        damage = random.randrange(1, 100)
        enemy = random.choice(ENEMY_OPTIONS)
        
        # Give player between 20 and 100 xp
        xp += random.randrange(20, 101)
        
        print(f"  In a run-in with a terrible {enemy} you suffer {damage} damage.")
        health -= damage

    if health > 0:
        caves_survived += 1
    press_enter()

clear()
print("YOU DIED. GAME OVER.")
print(f"Caves survived: {caves_survived}")
press_enter()
