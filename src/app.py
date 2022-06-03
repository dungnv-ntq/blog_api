from flask import Flask
from flask_restful import Api, Resource
from .config import app_config
from .views.UserView import user_api
from .models import db
from .resources.HelloWorld import HelloWorld
from .resources.StudentResource import StudentListResource, StudentResource


def create_app(env_name):
    """
    Create app
    :param env_name:
    :return:
    """

    app = Flask(__name__)
    app.config.from_object(app_config[env_name])
    db.init_app(app)

    api = Api(app)

    api.add_resource(HelloWorld, "/")
    api.add_resource(StudentListResource, "/students")
    api.add_resource(StudentResource, "/students/<student_id>")
    app.register_blueprint(user_api, url_prefix='/api/v1/users')

    return app
