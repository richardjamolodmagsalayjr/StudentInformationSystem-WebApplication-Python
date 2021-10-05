from flask import Blueprint, render_template, request, flash, redirect, url_for
import ssis_website.models as db
import re

course = Blueprint('course', __name__)

@course.route("/course")
def displayCoursePage():
    courses = db.Course.display_courses()
    college_options = db.College.get_colleges()
    return render_template("course_page.html", courses = courses, college_options = college_options)

@course.route("/course/add_course", methods=['GET', 'POST'])
def addCourse():
    if request.method == 'POST':
        college_code = request.form['college_code'].upper()
        course_code = request.form['course_code'].upper()
        course_name = request.form['course_name'].upper()

        try:
            if validateCourseCode(course_code):
                course = db.Course(course_code, course_name, college_code)
                course.add_course()
                flash("Course record was added successfully", "success")
            else:
                flash("Invalid course code, unable to add course record", 'danger')
        except:
             flash("Course code was already used, unable to add course record", 'danger')

    return redirect(url_for("course.displayCoursePage"))

@course.route("/course/edit_student", methods=["GET", "POST"])
def editCourse():
    if request.method == "POST":
        old_course_code = request.form['old_course_code'].upper()
        course_code = request.form['course_code'].upper()
        course_name = request.form['course_name'].upper()
        college_code = request.form['college_code'].upper()
        try:
            if validateCourseCode(course_code):
                db.Course.edit_course(course_code, course_name, college_code, old_course_code)
                flash("Course record was added successfully", "success")
            else:
                flash("Invalid course code, unable to add course record", 'danger')
        except:
             flash("Invalid course code, unable to add course record", 'danger')
       
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

def validateCourseCode(code):
    pattern1 = re.compile(r'BS\w{2}')
    pattern2 = re.compile(r'BS\w{1}')

    valid1 = re.fullmatch(pattern1, code)
    valid2 = re.fullmatch(pattern2, code)

    if valid1 or valid2:
        return True
    else:
        return False