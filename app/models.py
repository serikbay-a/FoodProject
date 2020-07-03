from app import db


class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    recipe = db.Column(db.String(1000), nullable=False)
    pic = db.Column(db.String(500), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(100), nullable=False)

    def __init__(self, name, recipe, pic, url, category):
        self.name = name
        self.recipe = recipe
        self.pic = pic
        self.url = url
        self.category = category

    def __repr__(self):
        return '<{} Recipe {}> category: {} pic: ({}) url: ({})'.format(self.id, self.name, self.category, self.pic, self.url)