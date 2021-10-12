from flask import render_template, request, flash, redirect, url_for
import ssis_website.models as db
import re
from . import student_bp
from ssis_website.student.student_form import StudentForm

@student_bp.route("/student", methods=['GET', 'POST'])
def displayStudentPage():
    form = StudentForm()
    students = db.Student.display_students()
    course_options = db.Course.get_course()
    gender_options = ["Male", "Female", "Other"]
    return render_template("student_page.html", students=students, course_options=course_options,
                            gender_options=gender_options, form=form)  

@student_bp.route("/student/add_student", methods=['GET', 'POST'])
def addStudent():
    form = StudentForm()
    if request.method == "POST":
        id_number = form.id_number.data
        firstname = form.firstname.data.upper()
        lastname = form.lastname.data.upper()
        course_code = request.form['course_code'].upper()
        year_level = int(request.form['year_level'])
        if request.form['gender'] == "Other":
            gender = request.form['gender_other']
        else:
            gender = request.form['gender']
        try:
            if validateIdNumber(id_number):
                student = db.Student(id_number, firstname, lastname, gender, year_level, course_code)
                student.add_student()
                flash('Student record was added succesfully!', 'success')
            else:
                flash('Invalid ID Number, unable to add student record! ', 'danger')
        except:
             flash('ID Number was already used! Unable to add student record! ', 'danger')
        
    return redirect(url_for('student.displayStudentPage'))

@student_bp.route("/student/edit_student", methods=['GET', 'POST'])
def editStudent():
    form = StudentForm()
    if request.method == "POST":
        old_id_number = request.form['old_id_number']
        id_number = form.id_number.data
        firstname = form.firstname.data.upper()
        lastname = form.lastname.data.upper()
        course_code = request.form['course_code'].upper()
        year_level = int(request.form['year_level'])
        if request.form['gender'] == "Other":
            gender = request.form['gender_other']
        else:
            gender = request.form['gender']
        try:
            if validateIdNumber(id_number):
                db.Student.edit_student(id_number, firstname, lastname, gender, year_level, course_code, old_id_number)
                flash('Student record was updated succesfully!', 'success')

            else:
                flash('Invalid ID Number, unable to update student record! ', 'danger')
        except:
             flash('ID Number was already used! Unable to update student record! ', 'danger')
        
    return redirect(url_for('student.displayStudentPage'))

@student_bp.route("/student/delete_student", methods=["POST"]) 
def deleteStudent():
    if request.method == "POST":
        student_id = request.form.get('student_id_del')
        db.Student.delete_student(student_id)
    
    return redirect(url_for("student.displayStudentPage"))

@student_bp.route("/student/search_student", methods=["GET","POST"])
def searchStudent():
    form = StudentForm()
    course_options = db.Course.get_course()
    gender_options = ["Male", "Female", "Gay", "Lesbain", "Bisexual"]
    if request.method == "POST":
        student_search_key = request.form['student_search_key']
        result = db.Student.search_student(student_search_key)
        if len(result) == 0:
            result = db.Student.display_students()
    return render_template("student_page.html", students=result, form=form, course_options = course_options,
                            gender_options = gender_options)

def validateIdNumber(id_number):
    pattern = re.compile(r'\d\d\d\d-\d\d\d\d')
    valid = re.fullmatch(pattern, id_number)
    
    return valid
               
            
       

            