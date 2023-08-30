from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db =SQLAlchemy()

class TextModel(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    texto = db.Column(db.String(80))


    def __init__(self, texto):
        self.texto = texto

    def __repr__(self):
        return f"{self.texto}"

class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

def create_table(app):
    with app.app_context():
        db.create_all()

def main():
    create_table()

if __name__ == "__main__":
    main()