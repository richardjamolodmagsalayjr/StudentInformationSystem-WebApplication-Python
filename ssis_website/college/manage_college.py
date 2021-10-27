from flask import render_template, request, flash, redirect, url_for
import ssis_website.models as db
import re 
from ssis_website.college.college_form import CollegeForm
from . import college_bp 
#college = Blueprint('college', __name__)

@college_bp.route("/college", methods = ["GET", "POST"])
def displayCollegePage():
    offset = 0
    if request.method == "POST":
        offset = int(request.form['offset'])

    form = CollegeForm()
    colleges = db.College.display_colleges(offset)
    return render_template("college_page.html", colleges = colleges, form = form)

@college_bp.route("/college/add_college", methods = ["GET", "POST"])
def addCollege():
    form = CollegeForm()
    if request.method == "POST":
        college_code = form.college_code.data.upper()
        college_name = form.college_name.data.upper()

        try:
            if validateCollegeCode(college_code):
                college = db.College(college_code, college_name)
                college.add_college()
                flash("College record was added successfully!", 'success')
            else:
                flash('Invalid college code, unable to update college record! ', 'danger')
        except:
            flash("College code was already used. Unable to add college record.", 'danger')

    return redirect(url_for("college.displayCollegePage"))

@college_bp.route("/college/delete_college", methods=["POST"]) 
def deleteCollege():
    if request.method == "POST":
        college_code_del = request.form.get('college_code_del')
        db.College.delete_college(college_code_del)
    
    return redirect(url_for("college.displayCollegePage"))

@college_bp.route("/college/edit_college", methods=["POST"]) 
def editCollege():
    form = CollegeForm()
    if request.method == "POST" and form.validate():
        old_college_code = request.form.get('old_college_code').upper()
        college_code = form.college_code.data.upper()
        college_name = form.college_name.data.upper()
      
        try:
            if validateCollegeCode(college_code):
                db.College.edit_college(college_code, college_name, old_college_code)
                flash("College record updated successfully!", 'success')
            else:
                flash('Invalid college code, unable to update college record! ', 'danger')
        except:
            flash("College code was already used, unable to update college record.", 'danger')
    
    return redirect(url_for("college.displayCollegePage"))


@college_bp.route("/college/search", methods=["GET","POST"])
def searchCollege():
    result = []
    form = CollegeForm()
    if request.method == "POST":
        college_search_key = request.form['college_search_key']
        if college_search_key == "" or college_search_key == None:
            result = []
        else:
            result = db.College.search_college(college_search_key)

    return render_template("college_page.html", colleges = result, form=form)

def validateCollegeCode(code):
    pattern1 = re.compile(r'C\w{2}')
    pattern2 = re.compile(r'C\w{3}')

    valid1 = re.fullmatch(pattern1, code)
    valid2 = re.fullmatch(pattern2, code)

    if valid1 or valid2:
        return True
    else:
        return False