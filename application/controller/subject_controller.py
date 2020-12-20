from application import app
from flask import render_template, current_app


@app.route("/subject")
def subject():

    return render_template("subject.html")
