from flask import Blueprint, render_template, request, flash, redirect, url_for
import ssis_website.models as db
import re 

college = Blueprint('college', __name__)

@college.route("/college")
def displayCollegePage():
    colleges = db.College.display_colleges()
    return render_template("college_page.html", colleges = colleges)

@college.route("/college/add_college", methods = ["GET", "POST"])
def addCollege():
    if request.method == "POST":
        college_code = request.form['college_code'].upper()
        college_name = request.form['college_name'].upper()

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

@college.route("/college/delete_college", methods=["POST"]) 
def deleteCollege():
    if request.method == "POST":
        college_code = request.form.get('college_code_del')
        db.College.delete_college(college_code)
    
    return redirect(url_for("college.displayCollegePage"))

@college.route("/college/edit_college", methods=["POST"]) 
def editCollege():
    
    if request.method == "POST":
        old_college_code = request.form.get('old_college_code').upper()
        college_code = request.form['college_code'].upper()
        college_name = request.form['college_name'].upper()
       

        try:
            if validateCollegeCode(college_code):
                db.College.edit_college(college_code, college_name, old_college_code)
                flash("College record added successfully!", 'success')
            else:
                flash('Invalid college code, unable to update college record! ', 'danger')
        except:
            flash("College code was already used, unable to add college record.", 'danger')
    
    return redirect(url_for("college.displayCollegePage"))


@college.route("/college/search", methods=["GET","POST"])
def searchCollege():
    result = []
    if request.method == "POST":
        college_search_key = request.form['college_search_key']
        result = db.College.search_college(college_search_key)

    return render_template("college_page.html", colleges = result)

def validateCollegeCode(code):
    pattern1 = re.compile(r'C\w{2}')
    pattern2 = re.compile(r'C\w{3}')

    valid1 = re.fullmatch(pattern1, code)
    valid2 = re.fullmatch(pattern2, code)

    if valid1 or valid2:
        return True
    else:
        return False