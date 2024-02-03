from flask import Flask, render_template
from flask import request
from random import randint
app = Flask(__name__)

global min_number
global max_number
global ai_number

min_number = 0
max_number = 1000
ai_number = randint(0, 1000)


def mathematics():
    return (min_number + max_number) // 2


@app.route('/winner.html',methods=['POST'])
def restart_game():
    return render_template('index.html')

#    return render_template('index.html')
#    user_number = int(request.form['user_number'])
#    math()


@app.route('/game.html', methods=['GET', 'POST'])
def math():
    global min_number
    global max_number
    global ai_number
    if request.method == 'POST':
        action = request.form['action']
        user_number = int(request.form['user_number'])
        ai_number = int(request.form['ai_number'])

        if (ai_number > user_number and action == 'small') or (ai_number < user_number and action == 'big') or ((ai_number != user_number) and action == 'same') or (ai_number == user_number  and (action == 'small' or action == 'big')):
            return render_template('game.html', user_number=user_number, ai_number=ai_number, min_number=min_number, max_number=max_number, show_text=True)

        else:
            if action == 'small':
                min_number = ai_number
                ai_number = mathematics()
                return render_template('game.html', user_number=user_number, ai_number=ai_number, min_number=min_number, max_number=max_number, show_text=False)

            elif action == 'big':
                max_number = ai_number
                ai_number = mathematics()
                return render_template('game.html', user_number=user_number, ai_number=ai_number, min_number=min_number, max_number=max_number, show_text=False)

            elif action == 'same':
                return render_template('winner.html', user_number=user_number)


@app.route('/index.html', methods=['POST'])
def user_number():
    global min_number
    global max_number
    global ai_number
    min_number = 0
    max_number = 1000

    ai_number = randint(0, 1000)
    user_number = int(request.form['user_number'])
    return render_template('game.html', ai_number=ai_number, user_number=user_number, min_number=min_number, max_number=max_number, show_text = False)


@app.route('/')
def index():
    return render_template('index.html')
#    global min_number
#    global max_number
#    global ai_number
#    min_number = 0
#    max_number = 1000
#
#    ai_number = randint(0, 1000)
#    return render_template('index.html')
#    user_number = int(request.form['user_number'])
#    math()


app.run(debug=True)
