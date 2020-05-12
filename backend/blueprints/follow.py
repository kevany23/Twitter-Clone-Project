from flask import (
    Flask, render_template, request, redirect,
    jsonify, Response, url_for, Blueprint
)
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, set_access_cookies, unset_access_cookies,
    get_raw_jwt
)

from database.database import *

FollowBlueprint = Blueprint('FollowBlueprint', __name__)

@FollowBlueprint.route('/findUsers', methods = ['GET'])
@jwt_required
def findUsers():
  accountLookup = Account.query.all()
  userId = get_jwt_identity()
  respQuery = {'users': []}
  for account in accountLookup:
    userData = {
      'id': account.id,
      'username': account.username,
    }
    # check if user is already following that account
    check = checkFollow(userId, account.id)
    if check:
      userData['following'] = True
    else:
      userData['following'] = False
    respQuery['users'].append(userData)
  return jsonify(respQuery)

@FollowBlueprint.route('/followUser', methods=['POST'])
@jwt_required
def handleFollowRequest():
  formData = request.get_json()
  toFollowLookup = Account.query.filter_by(username=formData['toFollow']).first()
  if toFollowLookup is None:
    return Response("Error", 400)
  toFollowId = toFollowLookup.id
  current_user = get_jwt_identity()
  if toFollowId == current_user:
    return Response("Same account Error", 400)
  success = followUser(current_user, toFollowId)
  if not success:
    return Response("Error3", 400)
  return Response("Success", 200)

@FollowBlueprint.route('/unfollowUser', methods=['POST'])
@jwt_required
def handleUnfollowRequest():
  formData = request.get_json()
  toUnfollowLookup = Account.query.filter_by(username=formData['toUnfollow']).first()
  if toUnfollowLookup is None:
    return Response("Error", 400)
  toUnfollowId = toUnfollowLookup.id
  current_user = get_jwt_identity()
  result = unfollowUser(current_user, toUnfollowId)
  if not result:
    return Response("Error", 400)
  return Response("Success", 200)


def checkFollow(userId, followingId):
  followLookup = Follow.query.filter_by(follower_id=userId, following_id=followingId).first()
  if followLookup is None:
    return False
  return True

def followUser(userId, followingId):
  # First check if user is already following that account
  followLookup = checkFollow(userId, followingId)
  if followLookup:
    #already exists
    return False
  newEntry = Follow(follower_id=userId, following_id=followingId)
  db.session.add(newEntry)
  db.session.commit()
  return True

def unfollowUser(userId, followingId):
  followLookup = Follow.query.filter_by(follower_id=userId, following_id=followingId).first()
  if followLookup is None:
    return False
  db.session.delete(followLookup)
  db.session.commit()
  return True
  