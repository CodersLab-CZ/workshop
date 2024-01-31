import random


def game():
    """The user should think of a number between 1 and 1000, and the computer should guess it.
    """
    min = 0
    max = 1000
    while True:
        guess = int((max-min)/2) + min
        print(f"Guessing: {guess}")
        answear = user_answear("I guessed?")
        if answear == True:
            print("I won!")
            break
        else:
            answear = user_answear("Too high?")
            if answear == True:
                max = guess
            else:
                answear = user_answear("Too low?")
                if answear == True:
                    min = guess
                else:
                    print("Don't cheat!")


def user_answear(question):
    """Returning answers to "Too small", "Too big", "You won".

    Args:
        question (string): one of the three questions on the result of the betting

    Returns:
        boolean: answer to question
    """
    while True:
        pick = input(f"{question} Answear yes or no: ")
        if pick == "yes":
            return True
            break
        elif pick == "no":
            return False
            break
        else:
            print("You have to choose yes or no")


print("Think about a number from 0 to 1000 and let me guess it!")

if __name__ == '__main__':
    game()
