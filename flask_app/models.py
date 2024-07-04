from . import db
from datetime import datetime


class APIHit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.String, nullable=False)
    request_type = db.Column(db.String, nullable=False)
    request_time = db.Column(db.DateTime, default=datetime.utcnow)
    payload = db.Column(db.JSON, nullable=True)
    content_type = db.Column(db.String, nullable=True)
    ip_address = db.Column(db.String, nullable=False)
    os = db.Column(db.String, nullable=False)
    user_agent = db.Column(db.String, nullable=False)
