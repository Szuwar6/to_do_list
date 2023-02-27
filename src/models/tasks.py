from src import db


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), nullable=False)
    details = db.Column(db.Text, nullable=True)
    author = db.Column(db.String(70), nullable=False)

