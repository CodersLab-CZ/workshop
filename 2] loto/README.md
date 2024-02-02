## LOTTO SIMULATOR

Simple console LOTTO application. The application gives 6 random numbers in range 1 - 49 and player is guessing them.


# Lauched application

Use the "cd" command to navigate to the "2] loto" folder and enter the command:

for LINUX
    python3 main.py

for WINDOWS
    python main.py


# Running application

1. The function gets the list numbers from a player and while checks:
- whether the entered text is a valid number,
- whether the user has not entered a given number before,
- if the number is in the range of 1-49.
2. The function uses randint (Random library) and gets a list of six original winning numbers in the range 1-49.
3. The function dislays list of numbers from player and list of winning numbers and then compares them.
4. The function displays how many numbers the player guessed.