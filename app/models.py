from app import db


class Recepie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.String(1000), nullable=False)
    URL_recepie = db.Column(db.String(500), nullable=False)
    category_food = db.Column(db.String(100), nullable=False)

def __init__(self, name, city, addr,pin):
   self.id = id
   self.name = name
   self.ingredients = ingredients
   self.URL_recepie = URL_recepie
   self.category_food = category_food