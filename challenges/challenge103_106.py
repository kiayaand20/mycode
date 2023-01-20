#!usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("practice.html")

@app.route("/correct")
def success():
    return f"You are correct! Great job!"

@app.route("/login", methods= ["POST"])
def login():
    if request.form.get("nm") and request.form.get("nm") == "Ruby":
        return redirect("/correct")
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
