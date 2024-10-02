import random
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def magic_8_ball():
    answers = [
        'It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes definitely.',
        'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Outlook good.',
        'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.',
        'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.',
        "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.",
        "Very doubtful."
    ]

    if request.method == "POST":
        question = request.form.get("question")
        if question:
            answer = random.choice(answers)
            return render_template("index.html", question=question, answer=answer)

    return render_template("index.html", question=None, answer=None)

if __name__ == "__main__":
    app.run(debug=True)
