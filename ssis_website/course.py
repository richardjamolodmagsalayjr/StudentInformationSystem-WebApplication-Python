from flask import Blueprint, render_template

course = Blueprint('course', __name__)

@course.route("/course")
def manage_course():
    return render_template("course_page.html")