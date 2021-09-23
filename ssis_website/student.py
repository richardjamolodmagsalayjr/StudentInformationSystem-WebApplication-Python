from flask import Blueprint, render_template

student = Blueprint('student', __name__)

@student.route("/student")
def manageStudent():
    return render_template("manage_student.html")  