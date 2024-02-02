import re
import random
#using regex and random to simulate the dice throw
def roll_dice(dice_code):
    pattern = r'(\d*)D(\d+)([-+]\d+)?'
    match = re.match(pattern, dice_code)

    try:
        num_rolls = int(match.group(1)) if match.group(1) else 1
        dice_type = int(match.group(2))
        modifier = int(match.group(3)) if match.group(3) else 0
        result = sum(random.randint(1, dice_type) for _ in range(num_rolls)) + modifier
        return result
    except AttributeError:
        return "Invalid dice"


print(roll_dice("2D10+10"))
print(roll_dice("D6"))
print(roll_dice("2D3"))
print(roll_dice("D12-1"))
print(roll_dice("XD1"))
