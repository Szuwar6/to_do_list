from flask.views import MethodView
from src.models.tasks import Tasks
from src.serializers.tasks import tasks_schema, task_schema


class ListAllTasksView(MethodView):
    methods = ["GET"]

    def get(self):
        tasks = Tasks.query.all()
        tasks_json = tasks_schema.dump(tasks)

        return tasks_json


class ListSpecificTaskView(MethodView):
    method = ["GET"]

    def get(self, id):
        task = Tasks.query.get(id)
        task_json = task_schema.dump(task)

        return task_json
