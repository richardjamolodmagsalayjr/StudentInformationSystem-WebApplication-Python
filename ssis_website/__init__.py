import os
from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    #app.config['SECRET_KEY'] = os.getenv['SECRET_KEY']

    from .views import views
    from .college import college
    from .course import course
    from .student import student

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(student, url_prefix="/")
    app.register_blueprint(course, url_prefix="/")
    app.register_blueprint(college, url_prefix="/")
    return app
