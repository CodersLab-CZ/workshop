from roll_the_dice import roll_the_dice

def calculate_points(points):
    """Calculate points.

    :param int points:

    :rtype: int
    :return: new_points
    """
    roll = roll_the_dice("2D6")
    if roll == 7:
        points //= 7
    elif roll == 11:
        points *= 11
    else:
        points += roll
    return points


def game_2001():
    """2001 game."""
    user_points = 0
    computer_points = 0

    input("Press ENTER to roll the dice")
    user_points += roll_the_dice("2D6")
    computer_points += roll_the_dice("2D6")

    while user_points < 2001 and computer_points < 2001:
        print(f"User points: {user_points}\nComputer points: {computer_points}")
        input("Press ENTER to roll the dice")
        user_points = calculate_points(user_points)
        computer_points = calculate_points(computer_points)

    print(f"User points: {user_points}\n Computer points: {computer_points}")
    if computer_points > user_points:
        print("Computer wins!")
    elif user_points > computer_points:
        print("User wins!")
    else:
        print("Draw")


if __name__ == '__main__':
    game_2001()

