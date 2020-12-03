from sqlalchemy.orm import relationship
from api_flask.model.db import db


class Api(db.Model):
    __tablename__ = "apis"
    id = db.Column(db.Integer, primary_key=True)
    api_name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    user = relationship("User") # ägaren/parent
    resources = relationship('Resource') # lista som api kommer åt



