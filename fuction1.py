from random import randrange


def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randrange(1, 7)
    return total

print(roll_dice(2))

