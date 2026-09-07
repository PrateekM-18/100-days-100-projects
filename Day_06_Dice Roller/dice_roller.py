import random


dice_faces = [
    """
┌───────┐
│       │
│   ●   │
│       │
└───────┘
""",

    """
┌───────┐
│ ●     │
│       │
│     ● │
└───────┘
""",

    """
┌───────┐
│ ●     │
│   ●   │
│     ● │
└───────┘
""",

    """
┌───────┐
│ ●   ● │
│       │
│ ●   ● │
└───────┘
""",

    """
┌───────┐
│ ●   ● │
│   ●   │
│ ●   ● │
└───────┘
""",

    """
┌───────┐
│ ●   ● │
│ ●   ● │
│ ●   ● │
└───────┘
"""
]


print("This is Dice Rolling Game")

def roll_dice():
    return random.randint(1,6)


while True:
    dice1 = roll_dice()
    dice2 = roll_dice()

    print(dice_faces[dice1-1],"       ",dice_faces[dice2-1])

    play_again = input("Do you want to play again? (y/n): ")

    if play_again != 'y':
        print("Thanks for playing")
        break
