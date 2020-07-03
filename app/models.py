from app import db


class Recepie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredients = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.String(1000), nullable=False)
    URL_recepie = db.Column(db.String(500), nullable=False)
    category_food = db.Column(db.String(100), nullable=False)

def __init__(self, name, city, addr,pin):
   self.name = name
   self.city = city
   self.addr = addr
   self.pin = pin