from flask import Blueprint

student_bp = Blueprint("student",__name__)

from . import manage_student