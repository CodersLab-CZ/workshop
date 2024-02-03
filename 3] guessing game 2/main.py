def computer_guess():
    print("Think of a number between 1 and 1000 and I'll guess it in no more than 10 moves.")
    print("Respond with 'Too small', 'Too big', or 'You win' after each of my guesses.")

    low = 1
    high = 1000
    guess = (low + high) // 2
    feedback = ''
    attempts = 0

    while feedback != 'You win' and attempts < 10:
        attempts += 1
        print(f"My guess is: {guess}.")
        feedback = input("Feedback: ").strip()

        if feedback == 'Too small':
            low = guess + 1
        elif feedback == 'Too big':
            high = guess - 1
        elif feedback == 'You win':
            print("Hooray! I guessed!")  # Updated message
            break
        else:
            print("Please enter a valid response ('Too small', 'Too big', 'You win').")
            attempts -= 1  # Invalid feedback doesn't count as an attempt

        guess = (low + high) // 2

    if feedback != 'You win':
        print("Seems like we've reached the max attempts or something went wrong. Did you cheat? 😉")


if __name__ == "__main__":
    computer_guess()


