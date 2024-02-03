from random import randint
import re

dices = ("3", "4", "6", "8", "10", "12", "20", "100")
dice_pattern = re.compile(r"^(\d*)D(\d+)([+-]\d+)?$")


def dice_throw():
    """
    dice_throw function takes input from user, confirming dice_pattern.
    Divide entry to multiply, modifier and dice, then calculate random throws and return value.
    :return:
    """
    command = input("Enter dice code:\n")
    match = dice_pattern.search(command)
    if not match:
        return "Wrong input"

    multiply, dice, modifier = match.groups()
    if dice not in dices:
        return "Wrong input"

    if multiply:
        multiply = int(multiply)
    else:
        multiply = 1

    if modifier:
        modifier = int(modifier)
    else:
        modifier = 0

    dice = int(dice)

    return sum([randint(1, dice) for _ in range(multiply)]) + modifier


if __name__ == '__main__':
    print(dice_throw())
