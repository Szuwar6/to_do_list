from src import db


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), nullable=False)
    details = db.Column(db.Text, nullable=True)
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    def __init__(self, id, title, details, author):
        self.id = id
        self.title = title
        self.details = details
        self.author = author


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(70), unique=True, nullable=False)

    tasks = db.relationship('Tasks', backref='users', lazy=True)

