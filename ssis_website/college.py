from flask import Blueprint, render_template

college = Blueprint('college', __name__)

@college.route("/college")
def manage_college():
    return render_template("college_page.html")