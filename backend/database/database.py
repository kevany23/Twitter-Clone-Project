from flask import g
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(500), nullable=False)
  timestamp = db.Column(db.DateTime, default=datetime.utcnow)
  username = db.Column(db.String(20), nullable=False)
  #follow = db.relationship("Follow", back_populates="Follow")
  def __repr__(self):
    return '<content %r>' % self.content

class Account(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), nullable=False)
  password = db.Column(db.String(20), nullable=False)

class Follow(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  #account = db.relationship("Account")
  follower_id = db.Column(db.String(20), db.ForeignKey(Account.id), nullable=False)
  following_id = db.Column(db.String(20), db.ForeignKey(Account.id), nullable=False)
  follower = db.relationship("Account", foreign_keys=[follower_id])
  following = db.relationship("Account", foreign_keys=[following_id])