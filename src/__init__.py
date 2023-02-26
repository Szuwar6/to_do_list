from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from src.config import Config


db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    from src.services.list import ListAllTasksView, ListSpecificTaskView
    from src.services.create import CreateTaskView

    app.add_url_rule('/api/tasks/list', view_func=ListAllTasksView.as_view("tasks_list"))
    app.add_url_rule('/api/task/<int:id>', view_func=ListSpecificTaskView.as_view("task_list"))

    app.add_url_rule('/api/task/create', view_func=CreateTaskView.as_view("task_create"))

    return app
