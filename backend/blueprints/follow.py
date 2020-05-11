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

@FollowBlueprint.route('/followUser', methods=['POST'])
@jwt_required
def handlefollowRequest():
  formData = request.get_json()
  print(formData['toFollow'])
  current_user = get_jwt_identity()
  print(current_user)
  accountLookup = Account.query.filter_by(username=formData['toFollow']).first()
  return Response("wip", 200)


def followUser():
  pass