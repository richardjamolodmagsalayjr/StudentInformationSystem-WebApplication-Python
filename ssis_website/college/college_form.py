from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CollegeForm(FlaskForm):
    college_code = StringField('College Code', validators=[DataRequired()])
    college_name = StringField('College Name', validators=[DataRequired()])
    add_college_button = SubmitField("Add College")
    edit_college_button = SubmitField("Update College")

    
    