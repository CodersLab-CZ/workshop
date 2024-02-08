import re
import random

def roll_dice(code):
    pattern = re.compile(r'(\d*)[dD]([3-9]|10|12|20|100)([+\-]\d+)?')

    match = pattern.match(code)
    if not match:
        return "Neplatny kod kostky."

    num_rolls = int(match.group(1)) if match.group(1) else 1
    dice_type = int(match.group(2))
    modifier = int(match.group(3)) if match.group(3) else 0

    result = sum(random.randint(1, dice_type) for _ in range(num_rolls)) + modifier

    return f"Vysledek hodu kostkou ({num_rolls}D{dice_type}{modifier}): {result}"

#priklad
kod_kostky = input("Zadejte kod kostky (napr. 2D10+10): ")
vysledek_hodu = roll_dice(kod_kostky)
print(vysledek_hodu)
