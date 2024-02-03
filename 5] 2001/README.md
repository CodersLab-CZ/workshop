## Number guessing game 2

Aplikace pro výpočet hodu kostkou ve formátu xDy+z kde:
x = počet hodů kostkou (nepovinné)
D = sympol pro označení druhu kostky (povinné)
y = označení kolikastěnná je kostka (povinné)
+z = modifikátor, který označí matematickou operaci, která se má s výsledkem hodu provést - povoleno je +, -, *, / (nepovinné)


# Lauched application

Use the "cd" command to navigate to the "5] 2001" folder and enter the command:

for LINUX
    python3 main.py

for WINDOWS
    python main.py


# Running application

1. Fukce přijme argument ve formátu strint a zkontroluje, zda byla použita správná kostka. Pokud ne, vrátí chybové hlášení.

2. Pokud ano, funkce se pokusí získat i další hodnoty. Kontroluje, zda byly zadány správně a pokud ne, vrátí chybové hlášení. 

3. Na základně zjištěních hodnot funkce vypočítá výsledek a vrátí ho ve formě int.
