from flask import render_template, request, flash, redirect, url_for
import ssis_website.models as db
import re
from . import course_bp
from ssis_website.course.course_form import CourseForm

from ssis_website import course


@course_bp.route("/course", methods=["GET","POST"])
def displayCoursePage():
    offset = 0
    if request.method == "POST":
        offset = int(request.form['offset'])

    form = CourseForm()
    courses = db.Course.display_courses(offset)
    college_options = db.College.get_colleges()
    return render_template("course_page.html", courses = courses, college_options = college_options, 
                            form = form)

@course_bp.route("/course/add_course", methods=['GET', 'POST'])
def addCourse():
    form = CourseForm()
    if request.method == 'POST':
        college_code = request.form['college_code']
        course_code = form.course_code.data.upper()
        course_name = form.course_name.data.upper()

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

@course_bp.route("/course/edit_student", methods=["GET", "POST"])
def editCourse():
    form = CourseForm()
    if request.method == "POST":
        old_course_code = request.form['old_course_code'].upper()
        course_code = form.course_code.data.upper()
        course_name = form.course_name.data.upper()
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

@course_bp.route("/course/delete_course", methods=["POST"]) 
def deleteCourse():
    if request.method == "POST":
        course_code = request.form.get('course_code_del')
        db.Course.delete_course(course_code)
    
    return redirect(url_for("course.displayCoursePage"))

@course_bp.route("/course/search", methods=["GET","POST"])
def searchCourse():
    form = CourseForm()
    result = []
    if request.method == "POST":
        course_search_key = request.form['course_search_key']
        if course_search_key == "" or course_search_key == None:
            result = []
        else:
            result = db.Course.search_course(course_search_key)

    return render_template("course_page.html", courses=result, form=form)

def validateCourseCode(code):
    pattern1 = re.compile(r'BS\w{2}')
    pattern2 = re.compile(r'BS\w{1}')

    valid1 = re.fullmatch(pattern1, code)
    valid2 = re.fullmatch(pattern2, code)

    if valid1 or valid2:
        return True
    else:
        return False