from flask import Flask, request

app = Flask(__name__)

HTML_START = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Hadejte cislo</title>
</head>
<body>
<h1>Myslete na cislo mezi 1 a 1000</h1>
<h3>Nerikejte vase cislo ;)</h3>
<form action="" method="POST">
    <input type="hidden" name="min" value="{}"></input>
    <input type="hidden" name="max" value="{}"></input>
    <input type="submit" value="OK">
</form>
</body>
</html>
"""


HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Hadejte cislo</title>
</head>
<body>
<h1>Je vase cislo {guess}?</h1>
<form action="" method="POST">
    <input type="submit" name="user_answer" value="prilis velke">
    <input type="submit" name="user_answer" value="prilis male">
    <input type="submit" name="user_answer" value="vyhral/a jste">
    <!-- <input type="submit" name="user_answer" value="vyhral/a jste"> -->
    <input type="hidden" name="min" value="{min}">
    <input type="hidden" name="max" value="{max}">
    <input type="hidden" name="guess" value="{guess}">
</form>
</body>
</html>
"""


HTML_WIN = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Hadejte cislo</title>
</head>
<body>
<h1>Huraaa! Uhodl jsem! Vase cislo je {guess}</h1>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def hadejte_cislo():
    if request.method == "GET":
        return HTML_START.format(0, 1001)
    else:
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))
        user_answer = request.form.get("user_answer")
        guess = int(request.form.get("guess", 500))

        if user_answer == "prilis velke":
            max_number = guess
        elif user_answer == "prilis male":
            min_number = guess
        elif user_answer == "vyhral/a jste":
            return HTML_WIN.format(guess=guess)

        guess = (max_number - min_number) // 2 + min_number

        return HTML.format(guess=guess, min=min_number, max=max_number)


if __name__ == '__main__':
    app.run()