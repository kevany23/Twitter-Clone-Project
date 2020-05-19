from flask import g
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Account(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), nullable=False)
  password = db.Column(db.String(20), nullable=False)


class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(500), nullable=False)
  timestamp = db.Column(db.DateTime, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey(Account.id), nullable=False)
  user = db.relationship("Account", foreign_keys=[user_id])
  def __repr__(self):
    return '<content %r>' % self.content

class Follow(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  follower_id = db.Column(db.String(20), db.ForeignKey(Account.id), nullable=False)
  following_id = db.Column(db.String(20), db.ForeignKey(Account.id), nullable=False)
  follower = db.relationship("Account", foreign_keys=[follower_id])
  following = db.relationship("Account", foreign_keys=[following_id])

  