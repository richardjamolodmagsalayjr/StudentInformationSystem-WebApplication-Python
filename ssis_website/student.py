from flask import Blueprint, render_template, request, flash, redirect, url_for
import ssis_website.models as db


student = Blueprint('student', __name__)

# database = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     port = "3306",
#     passwd= "password12345",
#     database = "information_system"
#     )
# cursor = database.cursor()

@student.route("/student", methods=['GET', 'POST'])
def displayStudentPage():
    students = db.Student.display_students()
    course_options = db.Course.get_course()
    return render_template("student_page.html", students=students, course_options=course_options)  

@student.route("/student/add_student", methods=['GET', 'POST'])
def addStudent():
    if request.method == "POST":
        id_number = request.form['id_number']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        gender = request.form['gender']
        course_code = request.form['course_code']
        year_level = int(request.form['year_level'])

        student = db.Student(id_number, firstname, lastname, gender, year_level, course_code)
        student.add_student()
        flash('Added student Successfully!', 'success')

    return redirect(url_for('student.displayStudentPage'))

# @student.route("/student/delete_student", methods=['GET', 'POST'])
# def deleteStudent():
#     if request.method == "POST":

