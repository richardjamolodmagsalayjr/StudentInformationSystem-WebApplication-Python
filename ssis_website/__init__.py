import os
from flask import Flask, render_template
#from flask_mysql_connector import MySQL
#from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    #app.config['SECRET_KEY'] = os.getenv['SECRET_KEY']
    # app.config.from_mapping(
    #     SECRET_KEY = SECRET_KEY,
    #     MYSQL_USER = DB_USERNAME,
    #     MYSQL_PASSWORD = DB_PASSWORD,
    #     MYSQL_DATABASE=DB_NAME,
    #     MYSQL_HOST=DB_HOST
    # )

    from .views import views
    from .college import college
    from .course import course
    from .student import student

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(student, url_prefix="/")
    app.register_blueprint(course, url_prefix="/")
    app.register_blueprint(college, url_prefix="/")
    return app
