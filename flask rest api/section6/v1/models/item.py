from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __str__(self):
        return str(self.item) + " " + str(self.price)

    def json(self):
        return {'name': self.item, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(item=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()