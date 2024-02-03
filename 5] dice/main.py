import re
import random
import sys

allow_rols =  {"3", "4", "6", "8", "10", "12", "20", "100"}

def parser(dice):
    return re.split(r'(\D+)', dice)


def roll_the_dice(roll):
    parts = parser(roll)

    if parts[0]:
       dice_roll = int(parts[0])
    else:
        dice_roll = 1

    if parts[1] != "D":
        print("Invalid dice Type")
        sys.exit()

    if parts[2] not in allow_rols: 
        print(f"Only allow dice type is: {','.join(allow_rols)}")
        sys.exit()

    dice_type = int(parts[2])
    total = 0

    for i in range(int(dice_roll)):
        result = (random.randint(1,int(dice_type)))
        total += result
    
    if len(parts) >= 5:   
      operation = parts[3]
      operation_number = int(parts[4])
      if operation == "+":
         total += int(operation_number)
      elif operation == "-":
         total -= int(operation_number)
       
    return total

print(roll_the_dice("2D6+1"))