from flask import Flask, render_template

app = Flask(__name__)

class DiceException(Exception):
    pass

def throw_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def play_turn():
    result = throw_dice()

    if result == 7:
        raise DiceException("// 7")
    elif result == 11:
        raise DiceException(" * 11")
    else:
        return result

def play_game():
    player_scores = [0, 0]

    while max(player_scores) < 2001:
        try:
            player_scores[0] += play_turn()
            player_scores[1] += play_turn()
        except DiceException as e:
            return None, str(e)

    winner = player_scores.index(max(player_scores)) + 1
    return winner, max(player_scores)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    winner, score = play_game()
    if winner is not None:
        return f"Hráč {winner} vyhrál s celkovým skóre {score}!"
    else:
        return f"Chyba: {score}"

if __name__ == "__main__":
    app.run(debug=True)

