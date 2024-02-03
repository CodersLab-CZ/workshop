from random import sample
import os

def print_fortune(fortune):
    os.system("clear")
    for i in range(0, len(fortune), 5):
        print(*fortune[i:i+5])

def select_number():
    os.system("clear")
#    fortune = [i for i in range(1,50)]
    fortune = list(range(1,50))
    select_numbers = []
    count = 0

#    while not count == 6:
    while count < 6:

       print_fortune(fortune)
       print("")
       print(f"Your select numbers are:")
       print(*select_numbers)
       select = input(f"Select {count + 1}. number out of 6, from 1 to 49: ")


       try:
           select = int(select)

           if 1 <= select <= 49:
               if select not in select_numbers:
                   select_numbers.append(fortune.pop(select - 1))
                   select_numbers.sort()
                   if (select - 1) >= 8:
                       fortune.insert(select - 1, "X ")
                       count += 1
                   else:
                       fortune.insert(select - 1, "X")
                       count += 1
    

       except ValueError:
           pass

    print_fortune(fortune)
    print("")
    print(f"Your select numbers are:")
    print(*select_numbers)


    random_indexes = sorted(sample(range(len(fortune)), 6))
    print("")
    print("The winning numbers are:")
    for lucky_numbers in random_indexes:
        print(lucky_numbers +1, end=" ")
    print("")

    sum_win_numbers = 0
    for index in random_indexes:
        if index <= 9 and fortune[index] == "X":
            print("X", end=" ")
            sum_win_numbers += 1        

        if index >= 10 and fortune[index] == "X ":
            print("X ", end=" ")
            sum_win_numbers += 1

        if index >= 10 and not fortune[index] == "X ":
            print("- ", end=" ")

        if index <= 9 and not fortune[index] == "X":
            print("-", end=" ")
        
    print("")
    if 6 >= sum_win_numbers >=3:
        return f"**** You won! ***\nYou guessed it.\nThe number of guessed numbers is {sum_win_numbers}"

    return f"Unfortunately, you didn't win.\nThe number of guessed numbers is less than 3.\nThe number of guessed numbers is {sum_win_numbers}."

print(select_number())
