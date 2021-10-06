from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class StudentForm(FlaskForm):
    id_number = StringField('ID Number', validators=[DataRequired()])
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    add_student_button = SubmitField("Add Student")
    edit_student_button = SubmitField("Update Student")

    
    