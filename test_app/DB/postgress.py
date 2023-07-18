from flask_sqlalchemy import SQLAlchemy
from  test_app.app import app
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Portnov1991@localhost:5432/pravoznayu'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200), nullable=False)
    correct_answer = db.Column(db.String(50), nullable=False)
    times_asked = db.Column(db.Integer, default=0)
    times_answered_correctly = db.Column(db.Integer, default=0)

