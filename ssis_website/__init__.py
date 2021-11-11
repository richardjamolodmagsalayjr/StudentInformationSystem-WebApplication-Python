import os
from flask import Flask
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, API_KEY, CLOUD_NAME, API_SECRET
from flask_wtf.csrf import CSRFProtect
import cloudinary
import cloudinary.uploader
import cloudinary.api

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
    cloudinary.config(
        cloud_name = CLOUD_NAME,
        api_key=API_KEY, 
        api_secret=API_SECRET,
        secure = True
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
