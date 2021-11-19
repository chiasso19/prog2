from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/meine-habits")
def meine_habits():
    return render_template('meine_habits.html')

@app.route("/heute")
def heute():
    return render_template('heute.html')

@ app.route("/statistik")
def statistik():
    return render_template('statistik.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)

