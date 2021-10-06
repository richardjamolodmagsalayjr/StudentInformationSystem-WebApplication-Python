from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CourseForm(FlaskForm):
    course_code = StringField('Course Code', validators=[DataRequired()])
    course_name = StringField('Course Name', validators=[DataRequired()])
    add_course_button = SubmitField("Add Course")
    edit_course_button = SubmitField("Update Course")
 
   
    