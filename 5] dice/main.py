import re
from random import randint as ri

def parse(code: str) -> tuple[str]:
    pattern = re.compile(r'(\d*)D(3|4|6|8|10|12|20|100)([+-]\d+)?')
    matched = pattern.match(code)
    
    if matched:
        rolls = int(matched.group(1)) if matched.group(1) else 1
        dice = int(matched.group(2))
        extras = int(matched.group(3)) if matched.group(3) else 0

        return rolls, dice, extras

    raise ValueError(f"The code {code} is invalid")


def simulate(code: str) -> int:
    try:
        rolls, dice, extras = parse(code)  
    except ValueError as ex:
        raise ValueError(f"The code '{code}' is invalid, simulation cannot continue.") from ex

    result = extras
    for _ in range(rolls):
        result += ri(1, dice)

    return result


if __name__ == "__main__":

    result = simulate("2D10+10")
