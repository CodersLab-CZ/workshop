import random
def zadej_cislo():
    while True:
        cislo = input("Your number (1-49): ")

        if not cislo.isdigit():
            print("It's not a number!")
            continue

        cislo = int(cislo)

        if cislo < 1 or cislo > 49:
            print("Number must be in range 1-49.")
            continue

        return cislo

def hra_lotto():
    vybrane_cisla = []
    for _ in range(6):
        cislo = zadej_cislo()
        while cislo in vybrane_cisla:
            print("This number is already chosen. Try another.")
            cislo = zadej_cislo()
        vybrane_cisla.append(cislo)

    vybrane_cisla.sort()
    print(f"Vybraná čísla: {vybrane_cisla}")

    vylosovana_cisla = random.sample(range(1, 50), 6)
    vylosovana_cisla.sort()
    print(f"Vylosovaná čísla: {vylosovana_cisla}")

    shodna_cisla = set(vybrane_cisla) & set(vylosovana_cisla)

    print(f"Počet shodných čísel: {len(shodna_cisla)}")
    print(f"Shodná čísla: {shodna_cisla}")


if __name__ == "__main__":
    hra_lotto()