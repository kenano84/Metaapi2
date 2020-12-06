from sqlalchemy.orm import relationship
from model.db import db
import model.models.endpoints


class Api(db.Model):
    __tablename__ = "apis"
    id = db.Column(db.Integer, primary_key=True)
    api_name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = relationship("User") # ägaren/parent
<<<<<<< HEAD
    endpoints = relationship("Endpoint")

    def to_dict(self):
        return {'id': self.id, 'api_name': self.api_name, 'description': self.description,
                'user_id': self.user_id, 'endpoints': [endpoints.to_dict() for endpoints in self.endpoints]}

=======
    resources = relationship('Resource') # lista som api kommer åt

    def to_dict(self):
        return {'user_id': self.id, 'username': self.username, 'password': self.password,
                'email': self.email, 'endpoints': [endpoints.to_dict() for endpoints in self.endpoints]}
>>>>>>> 27c13c892ce1ccbcd435bc03d1ca148967f97009
