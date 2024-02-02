from random import randint

user_input=[]
drawn_numbers=[]
matched=0
#system collects 6 different numbers in given range and sorts them
for x in range(6):
    while True:
        try:
            number = int(input(f"Input {x+1}. number in range 1-49: "))
            if number not in user_input and number in range(1,49):
                user_input.append(number)
                break
            else:
                print("Every number can be picked just once and must be in given range!")
        except ValueError:
            print("Input is not a number")
user_input.sort()
print(user_input)

#system draws 6 random numbers and sorts them
for x in range(6):
    while True:
        number = randint(1,49)
        if number not in drawn_numbers:
            drawn_numbers.append(number)
            break
drawn_numbers.sort()
print(drawn_numbers)

#system checks whether there are some matches in user input and system draws
for x in range(6):
    if user_input[x] in drawn_numbers:
        matched +=1
print(f'You matched {matched} number(s)')