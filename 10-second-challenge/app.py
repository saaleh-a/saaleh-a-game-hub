from flask import Flask, request, render_template
import time

app = Flask(__name__)

# Store the start time in memory (in a real app, use a more secure method like sessions or a database)
start_time = 0

@app.route("/", methods=["GET", "POST"])
def time_game():
    global start_time
    if request.method == "POST":
        # Handle when the user starts the timer
        if 'start' in request.form:
            start_time = time.time()
            return render_template("index.html", message="Timer started! Now press 'Stop' when you think 10 seconds have passed.", button="stop")

        # Handle when the user stops the timer
        elif 'stop' in request.form:
            end_time = time.time()
            users_time = end_time - start_time
            difference = abs(10 - users_time)

            if users_time == 10:
                result = "Well done! You were spot on!"
            elif 8 < users_time < 12:
                result = "You were close!"
            else:
                result = f"You were off by {difference:.1f} seconds."

            return render_template("index.html", result=result, guessed_time=users_time)

    # Default page
    return render_template("index.html", button="start", message="Press 'Start' when you're ready.")

if __name__ == "__main__":
    app.run(debug=True)
