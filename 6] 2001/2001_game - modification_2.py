"""
Workshop_01 - Program_05_Mod_2
--------------------------
2001 Game - Modification_2
--------------------------
(c) Tomas Dolejsek 2024-01-28

*** Modification 2 ***
Now try transferring your game to the server using Flask. To store information between turns, use hidden form fields.
This is not the best solution (may be prone to cheating), but we don't care about that for now. Dice selection before
the roll should be done using a form.
"""

from random import randint, choice
from flask import Flask, render_template, request, flash, session
from collections import namedtuple

app = Flask(__name__)
app.secret_key = "very secret key"
RoundResult = namedtuple('RoundResult', ['round', 'player', 'computer', 'winner'])


def calculate_roll(who: str, rolls: list[int, int]) -> int:
    """
    Pick two random numbers, each of range defined by type of dice. Return the sum.
    :param who: name of the participant of the roll ('Player' or 'Computer')
    :param rolls: list of dice types
    :return: score of the roll
    """
    x = randint(1, rolls[0])
    y = randint(1, rolls[1])
    flash(f"{who} picked D{rolls[0]} and D{rolls[1]}.")
    flash(f"{who}'s rolls: {x} + {y} = {x + y}")
    return x + y


def calculate_score(points: int, roll: int, round_number: int) -> int:
    """
    Calculate the outcome of the round. If important score is rolled (7 or 11), flash it out.
    :param points: current score
    :param roll: score in the current round
    :param round_number: number of a round
    :return: new score
    """
    if round_number == 1:
        return points + roll
    if roll == 7:
        flash("Points divided by 7!")
        return points // 7
    elif roll == 11:
        flash("Points multiplied by 11!")
        return points * 11
    else:
        return points + roll


def pick_computer_dice() -> tuple[int, int]:
    """
    Randomly pick two dice from the list of supported dice
    :return: two dice numbers
    """
    correct_dice = (3, 4, 6, 8, 10, 12, 20, 100)
    return choice(correct_dice), choice(correct_dice)


def play_round(round_number: int, score: dict, rolls: dict) -> namedtuple:
    """
    Plays one round and returns the outcome.
    :param round_number: NEXT round number
    :param score: dictionary of scores, both for player and computer
    :param rolls: dictionary of dices used for the given round
    :return: updated data after the round
    """
    limit = 2001
    winner = None
    flash(f"Recapitulation of previous round no. {round_number - 1}:")
    for member in score:
        roll = calculate_roll(member, rolls[member])
        score[member] = calculate_score(score[member], roll, round_number - 1)
        if score[member] >= limit:
            winner = member
            break
    return RoundResult(round=round_number, player=score['Player'], computer=score['Computer'],
                       winner=winner)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main module for index.html. On GET request, display basic page and set default values.
    On POST request, start the game, get values from forms and keep them updated according to the game rules.
    :return: None
    """
    rolls, score = dict(), dict()
    if request.method == 'GET':
        result = RoundResult(round=0, player=0, computer=0, winner=None)
        return render_template('index.html', results=result)
    if request.method == 'POST':
        round_number = int(request.form.get('round')) + 1  # next round
        winner = request.form.get('winner')
        if round_number > 1 and winner == 'None':
            score['Player'] = int(request.form.get('player_score'))
            score['Computer'] = int(request.form.get('computer_score'))
            dice1 = int(request.form.get('dice1'))
            dice2 = int(request.form.get('dice2'))
            rolls['Player'] = dice1, dice2
            rolls['Computer'] = pick_computer_dice()
            result = play_round(round_number, score, rolls)
        else:  # round ONE has different rules (7 and 11 don't matter)
            result = RoundResult(round=1, player=0, computer=0, winner=None)
        if result.winner:
            session['_flashes'].clear()  # clear flashes for the new game
        return render_template('game.html', results=result)


if __name__ == '__main__':
    app.run()
