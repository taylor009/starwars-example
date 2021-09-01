from models import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique = True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favorites = db.relationship('Favorite', backref='user')

    def __repr__(self):
        return '<User %r,%r,%r,%r>' % (self.id, self.user_name, self.email, self.password)

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email,
            "favorites": [favorite.serialize() for favorite in self.favorites]
        }