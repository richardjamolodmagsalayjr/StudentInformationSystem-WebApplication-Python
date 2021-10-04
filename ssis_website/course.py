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

@course.route("/course/edit_student", methods=["GET", "POST"])
def editCourse():
    if request.method == "POST":
        old_course_code = request.form['old_course_code'] 
        course_code = request.form['course_code'] 
        course_name = request.form['course_name']
        college_code = request.form['college_code']
        db.Course.edit_course(course_code, course_name, college_code, old_course_code)
    
    return redirect(url_for("course.displayCoursePage"))

@course.route("/course/delete_course", methods=["POST"]) 
def deleteCourse():
    if request.method == "POST":
        course_code = request.form.get('course_code_del')
        db.Course.delete_course(course_code)
    
    return redirect(url_for("course.displayCoursePage"))

@course.route("/course/search", methods=["GET","POST"])
def searchCourse():
    if request.method == "POST":
        course_search_key = request.form['course_search_key']
        results = db.Course.search_course(course_search_key)

    return render_template("course_page.html", courses=results)