from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "john": 85,
        "alice": 92,
        "bob": 78,
        "eve": 90,
        "charlie": 88,
        "dave": 80

    }
    return render_template("index.html", marks=marks)

app.run(debug=True)