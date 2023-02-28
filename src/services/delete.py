from flask.views import MethodView

from src import db
from src.models.tasks import Tasks


class DeleteTaskView(MethodView):
    methods = ["DELETE"]

    def delete(self, id):
        task = Tasks.query.get(id)
        if task is not None:
            db.session.delete(task)
            db.session.commit()
            return "Task has been deleted.", 200
        return "Task not found", 404
