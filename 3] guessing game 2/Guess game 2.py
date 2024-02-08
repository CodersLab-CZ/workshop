import random

def guessing_number2():
    print("Myslim na cislo mezi 1 a 1000.")
    nejnizsi = 1
    nejvyssi = 1000
    pokusy = 10

    for i in range(pokusy):
        hadane_cislo = random.randint(nejnizsi, nejvyssi)
        print(f"Pocitac hada: {hadane_cislo}")

        odpoved = input("Cislo je prilis male (m), prilis velke (v) nebo vyhravate (s): ")

        if odpoved == "m":
            nejnizsi = hadane_cislo + 1
        elif odpoved == "v":
            nejvyssi = hadane_cislo - 1
        elif odpoved == "s":
            print("Pocitac vyhral!")
            break
        else:
            print("Neplatna odpoved. Zadejte 'm' pro prilis male, 'v' pro prilis velke nebo 's' pro vyhravate.")

    else:
        print("Maximalni pocet pokusu. Vyhravate!")

if __name__ == "__main__":
    guessing_number2()