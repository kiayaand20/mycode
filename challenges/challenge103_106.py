#!usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app = Flask(__name__)

# grabs the vlaue or 'username' 
@app.route("/<username>")
def home_page(username):
    return render_template("practice.html", name = username)

# route for a correct answer
@app.route("/correct")
def success():
    return render_template("correct.html")

# route that allows user to POST answer
@app.route("/login", methods= ["POST", "GET"])
def login():
    if request.form.get("nm"):
        return redirect("/correct")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
