import random


def get_computer_numbers():
    """Get 6 random numbers from the range of 1 – 49

    Returns:
        set: 6 random numbers from the range of 1 – 49
    """
    numbers = set()
    while len(numbers) < 6:
        n = random.randint(1, 49)
        numbers.add(n)
    return numbers


def get_player_numbers():
    """Ask player for 6 numbers from the range of 1 – 49

    Returns:
        set: 6 random from the range of 1 – 49
    """
    numbers = set()
    while len(numbers) < 6:
        n = input(f"Guess 6 numbers from the range of 1 – 49: ")
        try:
            n = int(n)
        except ValueError:
            print("It's not a number!")
            continue
        if n in numbers:
            print(f"The {n} has already been entered")
        if not 1 <= n <= 49:
            print(f"The {n} is outside range the range of 1-49")
        else:
            numbers.add(n)
    return numbers


def game():
    """Start entering the player's numbers and view the result of the LOTTO game
    """
    player_numbers = get_player_numbers()
    print("The numbers you entered:", *sorted(list(player_numbers)))
    computer_numbers = get_computer_numbers()
    print("LOTTO drawn:", *sorted(list(computer_numbers)))

    match = len(player_numbers & computer_numbers)

    print("Number of guessed numbers:", match)


if __name__ == '__main__':
    game()
