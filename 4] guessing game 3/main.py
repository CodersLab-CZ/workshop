from flask import Flask, request

app = Flask(__name__)

HTML = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Guess My Number</title>
    </head>
    <body>
        <h2>Is your number {{ guess }}?</h2>
        <form action="/" method="post">
            <input type="hidden" name="min" value="{{ min }}">
            <input type="hidden" name="max" value="{{ max }}">
            <input type="hidden" name="guess" value="{{ guess }}">
            <button type="submit" name="answer" value="too_small">Too small</button>
            <button type="submit" name="answer" value="too_big">Too big</button>
            <button type="submit" name="answer" value="correct">You win</button>
        </form>
    </body>
    </html>
'''


@app.route('/', methods=['GET', 'POST'])
def guess():
    if request.method == 'POST':
        min_val = int(request.form.get('min', 1))
        max_val = int(request.form.get('max', 1000))
        guess = int(request.form.get('guess', 500))
        answer = request.form['answer']

        if answer == 'too_small':
            min_val = guess + 1
        elif answer == 'too_big':
            max_val = guess - 1
        elif answer == 'correct':
            return 'Congratulations! I guessed your number.'

        guess = (min_val + max_val) // 2
    else:
        min_val = 1
        max_val = 1000
        guess = (min_val + max_val) // 2

    return render_template_string(HTML, min=min_val, max=max_val, guess=guess)


if __name__ == '__main__':
    app.run(debug=True)
