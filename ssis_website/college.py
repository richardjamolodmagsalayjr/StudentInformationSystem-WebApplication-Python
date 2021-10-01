from flask import Blueprint, render_template, request, redirect, url_for
import ssis_website.models as db

college = Blueprint('college', __name__)

@college.route("/college")
def displayCollegePage():
    colleges = db.College.display_colleges()
    return render_template("college_page.html", colleges = colleges)

@college.route("/college/add_college", methods = ["GET", "POST"])
def addCollege():
    if request.method == "POST":
        college_code = request.form['college_code']
        college_name = request.form['college_name']
        college = db.College(college_code, college_name)
        college.add_college()

    return redirect(url_for("college.displayCollegePage"))