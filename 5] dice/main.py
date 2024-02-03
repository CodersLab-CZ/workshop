import re
import random


def simulate(code):
    """Calculate dice roll from dice with formula: xDy+z where:
    dice_type – type of dice to use (e.g. D6, D10),
    num_rolls – number of dice rolled; for a single roll this parameter is omitted,
    modifier – modifier - number to add (or subtract) to the result of the roll (optional).

    Args:
        code (string): the code entered for the simulation

    Raises:
        ValueError: given code is invalid

    Returns:
        int: result of simulation
    """
    types = [3, 4, 6, 8, 10, 12, 20, 100]
    match = re.fullmatch(r"(\d*)D(\d+)([+-]\d+)?", code)
    if not match:
        raise ValueError("Given code is invalid")
    num_rolls = int(match.group(1)) if match.group(1) else 1
    dice_type = int(match.group(2))
    if dice_type not in types:
        raise ValueError(
            "The value is not from D3, D4, D6, D8, D10, D12, D20, D100")
    modifier = int(match.group(3)) if match.group(3) else 0
    rolls = [random.randint(1, dice_type)for _ in range(num_rolls)]
    return sum(rolls)+modifier


code = input("Insert formula: ")
print(f"Result: {simulate(code)}")
