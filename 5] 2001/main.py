import re
import operator
import random


def simulate(code):
    """Calculate dice roll from dice with formula: xDy+z where:
    y – type of dice to use (e.g. D6, D10),
    x – number of dice rolled; for a single roll this parameter is omitted,
    z – modifier - number to add (or subtract) to the result of the roll (optional).

    Args:
        code (string): the code entered for the simulation

    Raises:
        ValueError: given code is invalid

    Returns:
        int: result of simulation
    """
    types = [3, 4, 6, 8, 10, 12, 20, 100]
    operations = {'+': operator.add, '-': operator.sub,
                  '*': operator.mul, '/': operator.truediv}
    try:
        x = re.findall('\d+(?=D)', code)
        x = int(x[0]) if x else 1
        y = re.findall('(?<=D)\d+', code)
        y = int(y[0]) if y else 0
        if y not in types:
            raise ValueError(
                "The value is not from D3, D4, D6, D8, D10, D12, D20, D100")
        op = re.findall('[+\\-/\\*]', code)
        op = str(op[0]) if op else "+"
        z = re.findall('(?<=[+-\/\\*])\d+', code)
        z = int(z[0]) if z else 0
    except:
        print("Given code is invalid")
    else:
        return operations[op](x * random.randint(1, y), z)


code = input("Insert formula: ")
print(f"Result: {simulate(code)}")
