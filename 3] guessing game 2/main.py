print("Mysli na číslo v rozmezí 1 - 1000 a já se pokusím jej uhodnout.")

#ověření švindlíře
my_number = int(input("Sem zadej své číslo: "))

#výchozí hodnoty
min = 0
max = 1000

#zacyklení hádání
x = 0

while x < 10:

    guess = int((max - min) // 2 + min)
    print(f"Je to číslo {guess}?")
    x += 1

    #dotaz na hodnotu
    answer = input("Zadej moc, málo nebo vyhráls: ")
    dictionary = {'moc':max, 'málo':min, 'vyhráls':True}
    allowed_answers = list(dictionary.keys())

    #pomínky pro správný proces
    if x == 10:
            print("Jsi švindlíř!!!")
    
    if answer in allowed_answers:
        if answer == 'moc':
            max = guess
        elif answer == 'málo':
            min = guess
        elif guess == my_number:
            print("Vyhrál jsi :D")
            break
        
    else:
        print(f"Neplatná odpověď zadej {', '.join(allowed_answers)}")
        x -= 1
