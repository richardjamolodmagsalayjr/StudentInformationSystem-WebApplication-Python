from flask import Blueprint, render_template

student = Blueprint('student', __name__)

@student.route("/student")
def displayStudent():
    return render_template("student_page.html")  

