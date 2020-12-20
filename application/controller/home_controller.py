from application import app
from flask import render_template, current_app


@app.route("/")
def home():

    return render_template("home.html")
