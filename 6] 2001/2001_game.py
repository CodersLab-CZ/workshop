"""
Workshop_01 - Program_05
---------
2001 Game
---------
(c) Tomas Dolejsek 2024-01-28

Implement the game of 2001. Below you will find the rules.

2001 – Game Rules
Each player starts with 0 points.
In their turn, a player rolls 2 dice (standard D6 dice). The number of obtained pips is added to the total score.
Starting from the second turn:
if a player rolls a 7, they divide their number of points by 7, disregarding the fractional part,
if the player rolls an 11, they multiply the current number of points by 11.
The player who first reaches 2001 points wins.

Implementation
Implement a two-player version of the game. It should be a console application. The other player should be a computer.
Display the current score after each turn.
The player's roll should take place when the user presses the enter key. The computer's roll occurs automatically,
after the player's roll. Terminate the program when either the player or the computer exceeds 2001 points.
"""

from random import randint


def calculate_roll(whose: str) -> int:
    """
    Pick two random numbers (1-6) and return the sum.
    :param whose: name of the participant of the roll ('Player' or 'Computer')
    :return: score of the roll
    """
    print(f"\n{whose}'s rolls: ", end='')
    x = randint(1, 6)
    y = randint(1, 6)
    print(f"{x} + {y} = {x + y}")
    return x + y


def calculate_score(points: int, roll: int, round_number: int) -> int:
    """
    Adjust score according to the rules. If important score is rolled (7 or 11),
    print a notification on the screen.
    :param points: current score
    :param roll: score is the current round
    :param round_number: number of a round
    :return: new score
    """
    if round_number == 1:
        return points + roll
    if roll == 7:
        print("Points divided by 7!")
        return points // 7
    elif roll == 11:
        print("Points multiplied by 11!")
        return points * 11
    else:
        return points + roll


def main():
    """
    Main module. Each ENTER pressed by user = new round. Keep going until player or computer wins the game.
    :return: None
    """
    print("Welcome to 2001 game!")
    score = {'Player': 0,
             'Computer': 0}
    round_number = 0
    winner = False
    while not winner:
        round_number += 1
        input(f"Press ENTER to start round no. {round_number}: ")
        for member in score:
            roll = calculate_roll(member)
            score[member] = calculate_score(score[member], roll, round_number)
            print(f"{member} score: {score[member]}")
            if score[member] >= 2001:
                print(f"{member} wins!")
                winner = True
                break


if __name__ == '__main__':
    main()
