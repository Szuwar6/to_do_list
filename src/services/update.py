from flask.views import MethodView
from flask import request
from src.models.tasks import Tasks
from src.serializers.tasks import task_schema
from src import db


class UpdateTaskView(MethodView):
    methods = ["PUT"]

    def put(self, id):
        body = request.get_json()
        task = Tasks.query.get(id)
        if task is not None:
            task = task_schema.load(body)
            db.session.merge(task)
            db.session.commit()
            return "Task has been updated.", 200

        return "Task not found.", 404
