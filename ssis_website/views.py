from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route("/")
@views.route("/homepage")
def home():
    return render_template("homepage.html")

@views.route("/others")
def others():
    return render_template("others.html")