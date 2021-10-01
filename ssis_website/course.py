from flask import Blueprint, render_template, request, redirect, url_for
import ssis_website.models as db

course = Blueprint('course', __name__)

@course.route("/course")
def displayCoursePage():
    courses = db.Course.display_courses()
    college_options = db.College.get_colleges()
    return render_template("course_page.html", courses = courses, college_options = college_options)

@course.route("/course/add_course", methods=['GET', 'POST'])
def addCourse():
    if request.method == 'POST':
        college_code = request.form['college_code']
        course_code = request.form['course_code']
        course_name = request.form['course_name']

        course = db.Course(course_code, course_name, college_code)
        course.add_course()

    return redirect(url_for("course.displayCoursePage"))


