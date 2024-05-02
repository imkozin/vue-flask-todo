from db import db

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(1000), nullable=False)


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(100), nullable=False)
