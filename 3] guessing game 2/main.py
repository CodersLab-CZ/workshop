import random


def game():
    """The user should think of a number between 1 and 1000, and the computer should guess it.
    The computer will make up to 10 guesses before declaring the user a cheater
    """
    min = 0
    max = 1000
    num_guesses = 0
    while True:
        guess = int((max-min)/2) + min
        print(f"I'm guessing {guess}, choose your answer")
        ans = get_user_answear()
        num_guesses += 1
        if num_guesses > 10:
            print("You are a cheater!")
            break
        elif ans == 1:  # Too small
            min = guess
        elif ans == 2:  # Too big
            max = guess
        else:
            print("I won!")
            break


def get_user_answear():
    """Gets the user's response to the current guess and validates input.

    Prompts the user to enter 1, 2 or 3 and repeats until valid.
    1 means the guess was too low. 
    2 means the guess was too high.
    3 means the guess was correct.

    Returns:
        int: The user's response code
    """

    while True:
        try:
            ans = int(input(
                """ 1) Too small\n 2) Too big\n 3) You win\n"""))
            if ans in [1, 2, 3]:
                break
            else:
                print("Please enter the number 1, 2 or 3")
        except ValueError:
            print("Please enter a number, not text")

    return ans


print("Think about a number from 0 to 1000 and let me guess it!")

if __name__ == '__main__':
    game()
