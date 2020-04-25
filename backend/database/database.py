from flask import g
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(500), nullable=False)
  timestamp = db.Column(db.DateTime, default=datetime.utcnow)
  username = db.Column(db.String(20), nullable=False)
  def __repr__(self):
    return '<content %r>' % self.content