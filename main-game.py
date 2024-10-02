from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__)

# Routes for each game
@app.route('/10-sec-challenge')
def ten_sec_challenge():
    return redirect('/10-sec-challenge')

@app.route('/magic-8-ball')
def magic_8_ball():
    return redirect('/magic-8-ball-flask')

@app.route('/rock-paper-scissors')
def rock_paper_scissors():
    return redirect('/rock-paper-scissors')

# Home route
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
