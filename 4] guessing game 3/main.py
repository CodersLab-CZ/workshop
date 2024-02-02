from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def guess_number():
    min_num = 0
    max_num = 1000
    count = 0

    #Flask post method that handles flow of values
    if request.method == 'POST':
        min_num = int(request.form.get('min'))
        max_num = int(request.form.get('max'))
        count = int(request.form.get('count'))
        answer = request.form['answer']
        count += 1

        # If the count of guesses reaches 10, user must be cheating, therefore system calls him liar
        if count == 10:
            return "Liar liar pants on fire!"

        if answer == "3":
            return "I won! Thanks for game"
        elif answer == "2":
            max_num = int((max_num - min_num) / 2) + min_num
        else:
            min_num = int((max_num - min_num) / 2) + min_num
    #counting number to guess
    guess = int((max_num - min_num) / 2) + min_num

    #template and variable handling
    return render_template('guess.html', min=min_num, max=max_num, count=count, guess=guess)

if __name__ == '__main__':
    app.run(debug=True)