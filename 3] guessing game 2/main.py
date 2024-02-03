def guessing_from_player():
    """
    guessing_from_player program ask player to think number from 0 to 1000
    then asking for value and react if too low, too high, or you guessed entered
    if not guessed in 10 round, player is cheating
    :return:
    """
    print("""Think about a number from 0 to 1000, and let me guess it!
    Press any key when you are ready""")
    input()
    round = 0
    min = 0
    max = 1000
    while round < 10:
        guess = int((max - min) / 2) + min
        print(f"Guessing: {guess}")
        answer = input("Enter too low, too high or you guessed:\n").lower()
        if answer == "you guessed":
            return print("I won!")
        elif answer == "too high":
            max = guess
            round += 1
        elif answer == "too low":
            min = guess
            round += 1
        else:
            print("Please enter only too low, too high or you guessed")
    print("Don't cheat!")


if __name__ == '__main__':
    guessing_from_player()
