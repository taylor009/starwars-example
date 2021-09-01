from models import db

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    entity_type = db.Column(db.String(255), unique=False, nullable=False)
    entity_id = db.Column(db.Integer, unique=False, nullable=False)
    user_name = db.Column(db.String(255), db.ForeignKey('user.user_name'))

    def __repr__(self):
        return '<Favorite %r,%r,%r,%r,%r>' % (self.id, self.name, self.entity_type, self.entity_id, self.user_name)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "entity_type": self.entity_type,
            "entity_id": self.entity_id,
            "user_name": self.user_name,
        }

