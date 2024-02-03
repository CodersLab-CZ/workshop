from random import randint
import os

min_number = 0
max_number = 1000

ai_number = randint(0, 1000)

def mathematics():
    return (min_number + max_number) // 2

def compare(ai_number, user_answer):
    global min_number, max_number

    if user_answer == 1:
        min_number = ai_number
        return mathematics()

    elif user_answer == 2:
        max_number = ai_number
        return mathematics()

def clear():
    os.system("clear")

def lyar():
    clear()  
    input(f"Don't cheat!\nPress Enter to continue...")


while True:
    try:
        clear()
        user_number = int(input(f"Think about a number from 1 to 1000 and let me guess it!\nPlease enter your number: "))
        if 1 <= user_number <= 1000:
            break
        else:
            clear()
            input(f"Please enter a number within the range of 1 to 1000.\nPress Enter to continue...")
    except ValueError:
        clear()
        input(f"Please enter a valid integer.\nPress Enter to continue...")

while True:
    clear()
    print(f"User number: {user_number}\n")
    print(f"AI guessed: {ai_number}\n")

    try:
        user_answer = int(input(f"Your answer for AI:\n\n1 for AI number is too low\n2 for AI number too high\n3 for AI number same with your\n\nEnter the number of answer: "))
        
        if user_answer not in [1, 2, 3]:
            input(f"Please enter 1, 2, or 3.\nPress Enter to continue...")

        if (ai_number > user_number and user_answer == 1) or (ai_number < user_number and user_answer == 2) or ((ai_number != user_number) and user_answer == 3) or (ai_number == user_number  and (user_answer == 1 or user_answer == 2)):
            lyar()

        elif user_answer in [1, 2]:
            ai_number = compare(ai_number, user_answer)
        else:
            clear()
            print(f"AI wins! Your number was {user_number}.")
            exit(0) 

    except ValueError:
        pass
