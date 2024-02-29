"""
Workshop_01 - Program_02
---------------
LOTTO Simulator
---------------
(c) Tomas Dolejsek 2024-01-30

LOTTO is a numeric game that involves drawing 6 numbers from the range of 1 – 49. The player's task is to correctly
guess the drawn numbers. You are rewarded if you correctly match 3, 4, 5 or 6 numbers.

Write a program that:

1. asks user to select 6 numbers, while checking the following conditions:
    - whether the string entered is a valid number,
    - whether the user has not entered a given number before,
    - if the number is in the range of 1-49,
2. after entering 6 numbers, sorts them in ascending order and displays them on the screen,
3. draws 6 numbers from the range and displays them on the screen,
4. informs the player how many numbers they have matched.
"""

from random import shuffle


class OutOfRangeError(Exception):
    def __init__(self, message):
        super().__init__(message)


class DuplicateNumberError(Exception):
    def __init__(self, message):
        super().__init__(message)


def get_numbers() -> set[int]:
    """
    Ask user for six numbers. For each number validate its type (int), range (1-49)
    and whether it hasn't been taken before.
    :return: set of user's numbers
    """
    n = 0
    numbers = []
    while n < 6:
        try:
            number = int(input(f"Enter {n + 1}. number (1 - 49): "))
            if not (1 <= number <= 49):
                raise OutOfRangeError("The number is out of range! Try again.")
            if number in numbers:
                raise DuplicateNumberError("You've already picked that number! Try again.")
            numbers.append(number)
            n += 1
        except ValueError:
            print("That's not a number! Try again.")
        except OutOfRangeError as e:
            print(e)
        except DuplicateNumberError as e:
            print(e)
    return set(numbers)


def lotto_picks() -> set[int]:
    """
    Pick six unique numbers from given range (1-49)
    :return: set of six random unique numbers
    """
    numbers = list(range(1, 50))
    shuffle(numbers)
    return set(numbers[:6])


def main():
    """
    Main module. Take six numbers from the user. Randomly pick six numbers as lotto picks.
    Print both lists in sorted order. Count matching numbers.
    :return: None
    """
    player = get_numbers()
    computer = lotto_picks()
    correct = len(player.intersection(computer))
    print(f"\nYou have picked these numbers: {' - '.join(map(str, sorted(player)))}")
    print(f"Computer picked these numbers: {' - '.join(map(str, sorted(computer)))}")
    print(f"You correctly picked {correct} number{'s' if correct != 1 else ''}.")


if __name__ == '__main__':
    main()
