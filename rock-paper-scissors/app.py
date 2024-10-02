from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def rps_game():
    result = None
    cpu_choice_name = None
    player_choice_name = None
    wins, losses = 0, 0

    if request.method == "POST":
        cpu_choice = random.randint(1, 3)  # CPU chooses Rock (1), Paper (2), or Scissors (3)
        player_choice = int(request.form.get("choice"))

        choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
        cpu_choice_name = choices[cpu_choice]
        player_choice_name = choices[player_choice]

        if player_choice == cpu_choice:
            result = "Tie!"
        elif player_choice == 1 and cpu_choice == 2:
            result = "You lose! Paper covers Rock!"
            losses += 1
        elif player_choice == 1 and cpu_choice == 3:
            result = "You win! Rock smashes Scissors!"
            wins += 1
        elif player_choice == 2 and cpu_choice == 3:
            result = "You lose! Scissors cuts Paper!"
            losses += 1
        elif player_choice == 2 and cpu_choice == 1:
            result = "You win! Paper covers Rock!"
            wins += 1
        elif player_choice == 3 and cpu_choice == 1:
            result = "You lose! Rock smashes Scissors!"
            losses += 1
        elif player_choice == 3 and cpu_choice == 2:
            result = "You win! Scissors cuts Paper!"
            wins += 1

    return render_template("index.html", result=result, cpu_choice=cpu_choice_name, player_choice=player_choice_name)

if __name__ == "__main__":
    app.run(debug=True)
