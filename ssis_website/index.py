from flask import Blueprint, render_template

index = Blueprint('index', __name__)

@index.route("/")
@index.route("/homepage")
def home():
    return render_template("homepage.html")
