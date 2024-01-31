from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def guess_the_number():
    """Number guessing game view
    
    Handles the game logic and rendering the template
    with the current state. Computer calculates next guess 
    based on human min/max values from requests.

    Returns:
        template: Rendered template view of game
    """
    if request.method == "GET":
        return render_template("index.html", state="start", min=0, max=1000)
    else:
        bingo = request.form["bingo"]
        if bingo == "true":
            return render_template("index.html", state="end")
        else:
            min = int(request.form["min"])
            max = int(request.form["max"])
            guess = int((max+min)/2)
            return render_template("index.html", state="guessing", guess=guess, min=min, max=max)


if __name__ == '__main__':
    app.run(debug=True)
