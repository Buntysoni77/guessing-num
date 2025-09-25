from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "secret123"  # required for session

@app.route("/", methods=["GET", "POST"])
def index():
    if "target" not in session:
        session["target"] = random.randint(1, 100)

    message = ""
    if request.method == "POST":
        try:
            user_choice = int(request.form["guess"])
            target = session["target"]

            if user_choice == target:
                message = f"🎉 Congratulations! You guessed {target} correctly. Game Over!"
                session.pop("target")  # reset game for next round
            elif user_choice < target:
                message = "⬇️ Oops! Too low, guess again."
            else:
                message = "⬆️ Oops! Too high, guess again."
        except:
            message = "⚠️ Please enter a valid number."

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
