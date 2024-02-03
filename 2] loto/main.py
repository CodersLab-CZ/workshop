from random import choice


def player_tip():
    """
    player_tip function ask player for 6 numbers from 1 to 49
    with validation for range, repetition and value
    """
    tip_list = []
    while len(tip_list) < 6:
        try:
            x = (int(input("Choose number from 1 to 49:\n")))
            if x not in tip_list and x in range(1, 50):
                tip_list.append(x)
            else:
                print("Please choose different number")
        except ValueError:
            print("Invalid number, try again")
    return sorted(tip_list)


def computer_tip():
    """
    computer_tip function draw 6 different numbers from 1 to 49
    """
    range_list = list(range(1, 50))
    c_tip_list = []
    while len(c_tip_list) < 6:
        y = choice(range_list)
        c_tip_list.append(y)
        range_list.remove(y)
    return sorted(c_tip_list)


def lotto():
    """
    lotto collects player_tip and computer_tip results and count
    similar tips
    """
    player_list = player_tip()
    computer_list = computer_tip()
    matched = 0
    for tip in player_list:
        if tip in computer_list:
            matched += 1
    print(f"Player tips :\n {player_list}")
    print(f"Computer tips :\n {computer_list}")
    print(f"You guessed {matched} number/s")


if __name__ == '__main__':
    lotto()
