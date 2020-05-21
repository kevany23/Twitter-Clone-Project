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

from datetime import datetime

from database.database import *
from blueprints.follow import getUserFollowing

PostBlueprint = Blueprint('PostBlueprint', __name__)

# Get posts from a certain user
def getUserPosts(userId):
    postLookup = Post.query.filter_by(user_id=userId).all()
    username = Account.query.filter_by(id=userId).one().username
    postList = []
    for post in postLookup:
        postJson = {
            'timestamp': post.timestamp,
            'content': post.content,
            'uid': userId,
            'username': username

        }
        postList.append(postJson)
    return postList

# Get posts from users
@PostBlueprint.route('/getPosts', methods=['GET'])
@jwt_required
def getFollowPosts():
    userId = get_jwt_identity()
    userList = getUserFollowing(userId)
    #userList.append({'userId': userId})
    userList.append({'userId': userId})
    posts = []
    for user in userList:
        print(user)
        uid = user['userId']
        userPosts = getUserPosts(uid)
        if not (userPosts is None):
            posts = posts + userPosts
    response = {'posts': posts}
    return jsonify(response)

@PostBlueprint.route('/submitPost', methods=['POST'])
@jwt_required
def submitPost():
    userId = get_jwt_identity()
    data = request.get_json()
    print(data)
    new_post = Post(content=data['content'], timestamp=datetime.now(),
        user_id=userId)
    db.session.add(new_post)
    db.session.commit()
    return Response("Success", 200)

# Sort in order
