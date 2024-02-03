from random import randint


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
        input("Press enter to throw")
        turn += 1
        player1 = d6_throw()
        player2 = d6_throw()
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
        return("Player WIN!")
    elif player2_points >= 2001:
        return ("Computer WIN!")


def d6_throw():
    """
    d6_throw represents 2 throws of D6 dices
    :return:
    """
    return randint(1, 6) + randint(1, 6)

print(game())