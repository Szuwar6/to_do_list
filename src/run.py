from src import create_app, db
from src.models.tasks import Tasks, Users


def create_db(app):
    with app.app_context():
        db.create_all()


def start_app():
    app = create_app()
    create_db(app)
    app.run(port=5000, host="0.0.0.0")


if __name__ == "__main__":
    start_app()
