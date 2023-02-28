from src import ma
from src.models.tasks import Tasks
from marshmallow import post_load


class TasksSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "details", "author")

    @post_load
    def create_task(self, data, **kwargs):
        return Tasks(**data)


task_schema = TasksSchema()
tasks_schema = TasksSchema(many=True)
