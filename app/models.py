from app import db


class Recepie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredients = db.Column(db.String(100), nullable=False)
    URL_recepie = db.Column(db.String(500), nullable=False)