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
            'id': post.id,
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
    processLikes(userId, posts)
    processComments(posts)
    response = {'posts': posts}
    return jsonify(response)

@PostBlueprint.route('/submitPost', methods=['POST'])
@jwt_required
def submitPost():
    userId = get_jwt_identity()
    data = request.get_json()
    new_post = Post(content=data['content'], timestamp=datetime.now(),
        user_id=userId)
    db.session.add(new_post)
    db.session.commit()
    return Response("Success", 200)

@PostBlueprint.route('/likePost', methods=['POST'])
@jwt_required
def handlePostLike():
    userId = get_jwt_identity()
    data = request.get_json()
    #check if like is already there
    lookup = PostLike.query.filter_by(post_id=data['postId'], account_id=userId).first()
    if not (lookup is None):
        return Response("Already liked", 400)
    new_like = PostLike(post_id = data['postId'], account_id=userId)
    db.session.add(new_like)
    db.session.commit()
    return Response("Success", 200)

@PostBlueprint.route('/unlikePost', methods=['POST'])
@jwt_required
def handlePostUnlike():
    userId = get_jwt_identity()
    data = request.get_json()
    lookup = PostLike.query.filter_by(post_id=data['postId'], account_id=userId).first()
    if lookup is None:
        return Response("Nothing to unlike", 400)
    db.session.delete(lookup)
    db.session.commit()
    return Response("Success", 200)

#Helper to process user liked posts so they can be shown on page load
def processLikes(userId, posts):
    for post in posts:
        likeLookup = PostLike.query.filter_by(post_id=post['id'], account_id=userId).first()
        if likeLookup is None:
            post['liked'] = False
        else:
            post['liked'] = True

#Helper to insert comments for each post
def processComments(posts):
    for post in posts:
        #Lookup the comment
        commentLookup = Comment.query.filter_by(post_id=post['id']).order_by(Comment.timestamp).all()
        post['comments'] = []
        if commentLookup is None:
            continue
        for comment in commentLookup:
            #Look up user
            accountLookup = Account.query.filter_by(id=comment.account_id).one()
            post['comments'].append({
                'content': comment.content,
                'username': accountLookup.username
            })
    

@PostBlueprint.route('/submitComment', methods=['POST'])
@jwt_required
def handleComment():
    userId = get_jwt_identity()
    data = request.get_json()
    postId = data['postId']
    content = data['content']
    #Validate postId
    postLookup = Post.query.filter_by(id=postId)
    if postLookup is None:
        return Response("Invalid Post", 400)
    comment = Comment(post_id=postId, account_id=userId, timestamp=datetime.now(), content=content)
    db.session.add(comment)
    db.session.commit()
    return Response("Success", 200)
