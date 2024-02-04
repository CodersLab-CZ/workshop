from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('welcome.html') 

min = 0
max = 1000
guess = (max - min) // 2 + min

@app.route('/index', methods=['GET', 'POST'])
def game():

    global min, max, guess
    
    print(guess)
    print(min, max)
    
    if request.method == 'POST':
        # Získání hodnot z formuláře
        action = request.form['action']
        # Aktualizace rozsahu podle odpovědi uživatele
        if action == 'Příliš malé':
            min = guess
        elif action == 'Příliš velké':
            min = guess
        elif action == 'Vyhráváte':
            return win()
        # Výpočet nového odhadu
        guess = (max - min) // 2 + min
        
    # Renderování šablony s aktuálními hodnotami pro hru
    return render_template('index.html', guess=guess, min=min, max=max)

@app.route('/win')
def win():
    return render_template('win.html', guess=guess)  # Zobrazení stránky pro vítězství

if __name__ == '__main__':
    app.run(debug=True)