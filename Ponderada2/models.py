from flask_sqlalchemy import SQLAlchemy

db =SQLAlchemy()

class TextModel(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    texto = db.Column(db.String(80))

    def __init__(self, texto):
        self.texto = texto

    def __repr__(self):
        return f"{self.texto}"