from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def dashboard():
    data = {
        "voltage": round(random.uniform(210, 240), 2),
        "current": round(random.uniform(5, 20), 2),
        "power": round(random.uniform(1, 5), 2),
        "frequency": round(random.uniform(49.5, 50.5), 2)
    }
    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
