from random import randint, choice

dices = ("D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100")


def dice_throw():
    """
    dice_throw function takes input from user, confirming existing dice.
    After that simulate throw of dice. 2 choices of dice and throws in total.
    :return:
    """
    result = 0
    throw = 0
    while throw < 2:
        for take in range(2):
            command = input("Enter dice code D3, D4, D6, D8, D10, D12, D20 or D100:\n")
            if command not in dices:
                print("Wrong input")
            else:
                dice = int(command.removeprefix("D"))
                result += randint(1, dice)
                throw += 1
    return result


def comp_dice_throw():
    """
    comp_dice_throw simulates random choice of 2 dices and throw
    :return:
    """
    result = 0
    for take in range(2):
        command = choice(dices)
        dice = int(command.removeprefix("D"))
        result += randint(1, dice)
    return result


def game():
    """
    game is 2001 game with throwing 2 D6 dices, adding throw value to score.
    From second turn if roll is 7 then divide score by 7, if 11, multiply score by 11.
    First player who hit or exceeded 2001 wins
    :return:
    """
    player1_points = 0
    player2_points = 0
    turn = 0
    while player1_points < 2001 and player2_points < 2001:
        turn += 1
        player1 = dice_throw()
        player2 = comp_dice_throw()
        if turn >= 2 and player1 == 7:
            player1_points = player1_points // 7
        elif turn >= 2 and player1 == 11:
            player1_points = player1_points * 11
        else:
            player1_points += player1

        if turn >= 2 and player2 == 7:
            player2_points = player2_points // 7
        elif turn >= 2 and player2 == 11:
            player2_points = player1_points * 11
        else:
            player2_points += player2
        print(f"Player points : {player1_points}")
        print(f"Computer points : {player2_points}")
    if player1_points >= 2001:
        return "Player WIN!"
    elif player2_points >= 2001:
        return "Computer WIN!"


if __name__ == '__main__':
    print(game())
