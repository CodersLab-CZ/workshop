def get_answer() -> str:
    """
    A function for getting player's answer.

    A function gets the player's answer and chcek if
    it is in the list of correct answers. If it is, it 
    return answer as string. If it is not, the function
    starts again.
    """
    # getting an answer
    answer = input("(ALLOWED ANSWERS: too low / too high / "
                    "you quessed):\n")

    # answer check
    correct_answers = ["too low", "too high", "you quessed"]
    if answer in correct_answers:
        return answer
    else:
        print("Wrong value, try again...") 
        get_answer()


def main():
    """
    A function for guessing a number.

    The function uses a math formula for getting most
    likely numbers in the range 0 - 1000. Then the function
    uses get_answer() for information, if is the number correct,
    too hight or too low. 
    If the quessed number is not correct, the function change
    numbers for calculation and repeats the process.
    If the game is fair, the PC guesses the number within ten cycles.
    """
    # hello area
    print("Think about a number from 0 do 1000 and "
          f"let me guess it!\n{'=' * 56}")

    min = 0
    max = 1000
    num_of_tries = 10

    while num_of_tries:
        # calculation of the quessed number
        guess = (max-min) // 2 + min
        print(f"Guessing: {guess}. Am I right?")
        print(f"Pokus {num_of_tries}")

        # processing the player's response
        answer = get_answer()
        if answer == "too high":
            max = guess
            num_of_tries -= 1
        elif answer == "too low":
            min = guess
            num_of_tries -= 1
        elif answer == "you quessed":
            print("I won!")
            num_of_tries = 0
          
          
main()