from sqlalchemy.orm import relationship
from api_flask.model.db import db


class Endpoint(db.Model): # child till apis
    __tablename__ = "endpoints"
    id = db.Column(db.Integer, primary_key=True)
    uri = db.Column(db.String(100), nullable=False)
    api_id = db.Column(db.Integer, db.ForeignKey("apis.id"))
    apis = relationship("Api")

