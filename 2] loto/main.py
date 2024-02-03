from random import randint

def comparsion(user_number, pc_number):
    """ The function compare pc_number and user_number and return result of comparsion."""

    if user_number < pc_number:
        return "Too small!"

    elif user_number > pc_number:
       return "Too big!"

    return "You win!"

pc_number = randint(1,100)
print(pc_number)

win=""
while win !=  "You win!":
     print(f"Guess the number from 1 to 100.")
     user_number = input("Guess the number: ")

     try:
         user_number = int(user_number)

         if not 0 <= user_number <= 101:
            print(f"It's not a number from 1 to 100!")
         else:
            win = comparsion(user_number, pc_number)
            print(win)     

     except ValueError:
         print(f"It's not a number!")
