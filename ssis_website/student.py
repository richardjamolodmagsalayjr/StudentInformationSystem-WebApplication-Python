from flask import Blueprint, render_template, request, flash, redirect, url_for
import ssis_website.models as db


student = Blueprint('student', __name__)


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

@student.route("/student/edit_student", methods=['GET', 'POST'])
def editStudent():
    if request.method == "POST":
        old_id_number = request.form['old_id_number']
        id_number = request.form['id_number']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        gender = request.form['gender']
        course_code = request.form['course_code']
        year_level = int(request.form['year_level'])
        
        db.Student.edit_student(id_number, firstname, lastname, gender, year_level, course_code, old_id_number)

    return redirect(url_for('student.displayStudentPage'))

@student.route("/student/delete_student", methods=["POST"]) 
def deleteStudent():
    if request.method == "POST":
        student_id = request.form.get('student_id_del')
        db.Student.delete_student(student_id)
    
    return redirect(url_for("student.displayStudentPage"))

@student.route("/student/search_student", methods=["GET","POST"])
def searchStudent():
    if request.method == "POST":
        student_search_key = request.form['student_search_key']
        result = db.Student.search_student(student_search_key)

    return render_template("student_page.html", students=result)