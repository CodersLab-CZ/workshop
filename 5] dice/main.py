import re
from random import randint

def roll(kostky):

    #zde jsou pomocné proměnné pro parsovani
    x = re.findall("(\d+)D", kostky)
    if not x:
        x = "1"
    y = re.findall("D(\d+)", kostky)
    if not any(hodnota in y for hodnota in ['3', '4', '6', '8', '10', '12', '20', '100']):
        return "Neplatná hodnota"
    z = re.findall("\+(\d+)", kostky)
    if not z:
        z = "0"
    d = re.findall("\-(\d+)", kostky)
    if not d:
        d = "0"

    #převod proměnných na čísla
    pocet = int(x[0])
    hrany = int(y[0])
    plus = int(z[0])
    minus = int(d[0])

    #vypočet počtu kostek a hran
    cisla = 0
    for hody in range(pocet):
        cislo = randint(1, hrany)
        cisla += cislo
    #vysledná suma i s modifikatorem
    vysledek = cisla + plus - minus

    return vysledek

print(roll("5D10+20"))