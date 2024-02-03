from flask import Flask, request, render_template
import random


app = Flask(__name__)


def calculate_points(total_points, current_points):
    """Calculate score based on dice roll and previous score.

    Applies special rules if current points are 7 or 11.
    Adds current points to total if no rules apply.

    Args:
        total_points (int): The previous total score
        current_points (int): Points scored in current roll

    Returns:
        int: The updated score
    """
    if total_points == 0:
        return current_points
    elif current_points == 7:
        return int(total_points / 7)
    elif current_points == 11:
        return int(total_points * 11)
    else:
        return total_points + current_points


@app.route("/", methods=["GET", "POST"])
def start_game():
    """Start view to play a new game

    Returns the rendered template with updated score
    or initial empty scoreboard.

    Returns:
        template: Rendered index.html template
    """
    if request.method == "GET":
        return render_template("index.html", score_computer=0, score_human=0)
    else:
        score_human = int(request.form["score_human"])
        score_computer = int(request.form["score_computer"])
        human_sum_of_dices = int(
            request.form["firstDice"]) + int(request.form["secondDice"])
        dice_types = [3, 4, 6, 8, 10, 12, 20, 100]
        computer_sum_of_dices = int(random.choice(
            dice_types)) + int(random.choice(dice_types))
        score_computer = calculate_points(
            score_computer, random.randint(2, computer_sum_of_dices))
        score_human = calculate_points(
            score_human, random.randint(2, human_sum_of_dices))
        return render_template("index.html", score_computer=score_computer, score_human=score_human)


if __name__ == '__main__':
    app.run(debug=True)
