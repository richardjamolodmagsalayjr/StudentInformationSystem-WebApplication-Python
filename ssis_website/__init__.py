from flask import Flask, render_template
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv['SECRETKEY']
    from .views import views
    # from .college import college
    # from .course import course
    # from .student import student

    app.register_blueprint(views, url_prefix="/")

    return app
