import os
from flask import Flask
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY
from flask_wtf.csrf import CSRFProtect

#CSRFProtect()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
   
    
    app.config.from_mapping(
        SECRET_KEY = SECRET_KEY,
        MYSQL_USER = DB_USERNAME,
        MYSQL_PASSWORD = DB_PASSWORD,
        MYSQL_DATABASE=DB_NAME,
        MYSQL_HOST=DB_HOST
    )
    CSRFProtect(app)
    
    from .index import index
    from .college import college_bp
    from .course import course_bp
    from .student import student_bp

    app.register_blueprint(index, url_prefix="/")
    app.register_blueprint(student_bp, url_prefix="/")
    app.register_blueprint(course_bp, url_prefix="/")
    app.register_blueprint(college_bp, url_prefix="/")

    return app
