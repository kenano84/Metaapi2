import sqlalchemy as sa
from sqlalchemy.orm import relationship 

from model.db import db


class User(db.Model): # parent till apis
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    # apis = relationship("Api")

    def to_dict(self):
        return {'user_id': self.id, 'username': self.username, 'password': self.password,
                'email': self.email}

                #  , 'apis': self.apis}
                # apis hur? det är en lista?


