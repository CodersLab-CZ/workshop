from random import randint

def tips():
    player1 = randint(1, 100)
    while True:  
        try:
            player2 = int(input("Hádej číslo: "))
            if player1 > player2:
                print("Příliš malé")
                continue
            elif player2 > player1:
                print("Příliš velké")
                continue
            else:
                print("Vyhráváš")
                break
        except:
            print("Toto není číslo!")
        
tips()