from flask.views import MethodView
from flask import request

from src.serializers.tasks import task_schema
from src.models.helpers import save_to_db

import json


class CreateTaskView(MethodView):
    methods = ["POST"]

    def post(self):
        body = request.data
        task = task_schema.loads(json.dumps(body))

        save_to_db(task)

        return "Task's been created successfully!", 201