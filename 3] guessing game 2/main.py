print("Think about a number from 0 to 1000 and let me guess it!")

answer = ""
min = 0
max = 1000
count = 0

#the cycle continues till the guess is correct
while answer != "3":

    guess = int((max - min) / 2) + min

    #If the count of guesses reaches 10, user must be cheating, therefore system calls him liar
    #Otherwise system cointinues guessing
    if count == 10:
        print("Liar liar pants on fire!")
        break
    else:
        print(f"Guessing: {guess}")
        count += 1

    #user inputs a number to give a clue to the system
    answer = input("Your verdict 1 - Too small, 2 - Too big, 3 - You win => ")

    if answer == "3":
        print("I won! Thanks for game")
    elif answer == "2":
        max = guess
    else:
        min = guess
