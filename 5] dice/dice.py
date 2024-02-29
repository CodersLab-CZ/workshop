"""
Workshop_01 - Program_05
----
Dice
----
(c) Tomas Dolejsek 2024-01-30

Board games and pen-and-paper RPG games use many types of dice, not just the well-known cubic ones.
One of the most popular dice are, for example, a ten-sided one or even a hundred-sided one! Since dice are often tossed
in games, writing "e.g. roll two ten-sided dice and add 20 to the result" each time would be boring, difficult,
and wasting huge amounts of paper. In such situations, the code "roll 2D10+20" is used.

The code for such a die has the following formula: xDy+z
where:
    * y – type of dice to use (e.g. D6, D10),
    * x – number of dice rolled; for a single roll this parameter is omitted,
    * z – modifier - number to add (or subtract) to the result of the roll (optional).

Examples:

2D10+10: roll 2 D10 dice, add 10 to the result,
D6: a single roll of a cubic die,
2D3: roll 2 three-sided dice,
D12-1: roll one D12 die, subtract 1 from the result.
Write a function that will:

take such code as a string in the parameter,
recognize all input data:
    * type of dice,
    * number of rolls,
    * modifier,
return an appropriate message if the given string is invalid,
simulate the rolls and return the result.
Types of dice used in games: D3, D4, D6, D8, D10, D12, D20, D100.
"""

import re
from random import randint
from collections import namedtuple
DiceRoll = namedtuple('DiceRoll', ['number', 'dice', 'modifier'])


class InvalidInputError(Exception):
    def __init__(self):
        super().__init__()


def process_input(user: str) -> namedtuple:
    """
    Take user's input and validate its correctness. If it's not correct, return False.
    Using regex expression, extract needed information (number of rolls, type of dice and modifier).
    Return the result as namedtuple.
    :param user: string given by user
    :return: False if incorrect input or namedtuple with extracted info (number of rolls, type of dice, modifier)
    """
    pattern = re.compile(r'^([0-9]*)D(3|4|6|8|10|12|20|100)([+-][0-9]+)?$')
    matches = pattern.match(user)

    if not matches:
        raise InvalidInputError

    rolls = int(matches.group(1) or 1)
    dice = int(matches.group(2))
    modifier = int(matches.group(3) or 0)

    return DiceRoll(number=rolls, dice=dice, modifier=modifier)


def calculate_roll(roll: namedtuple) -> int:
    """
    Take roll data and calculate the outcome.
    :param roll: roll data (number of rolls, type of dice and modifier)
    :return: result of a roll
    """
    suma = roll.modifier
    print("Rolls: ", end='')
    for _ in range(roll.number):
        x = randint(1, roll.dice)
        print(f"{x} ", end='')
        suma += x
    return suma


def main():
    """
    Main module. Take input from the user and print the result.
    :return: None
    """
    while True:
        try:
            user = input("Enter roll in a form xDy+z: ").upper()
            roll = process_input(user)
            print(f"\nThe result of a {user} dice roll is: {calculate_roll(roll)}")
            break
        except InvalidInputError:
            print("Incorrect input!")


if __name__ == '__main__':
    main()
