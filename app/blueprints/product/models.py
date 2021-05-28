from app import db
from datetime import datetime
from app.blueprints.auth.models import User


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(300))
    price = db.Column(db.Numeric(6,2))
    image = db.Column(db.String(200))

    def __init__(self, name, description, price, image):
        self.name = name
        self.description = description
        self.price = price
        self.image = image

    def __repr__(self):
        return f'<Product | {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': str(self.price),
            'image': self.image
        }

    def from_dict(self, data):
        for field in ['id', 'name', 'description', 'price', 'image']:
            if field in data:
                setattr(self, field, data[field])

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()        