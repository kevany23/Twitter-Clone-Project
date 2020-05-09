from flask import (
    Flask, render_template, request, redirect,
    jsonify, Response, url_for
)
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, set_access_cookies, unset_access_cookies,
    get_raw_jwt
)

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = "8AGEsKUC7cjfScOAScfDiQgX"
CORS(app)

class User:
  pass


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.config['JWT_SECRET_KEY'] = "8AGEsKUC7cjfScOAScfDiQgX"
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
jwt = JWTManager(app)
blacklist = set()

from database.database import *
db.init_app(app)
db.app = app
db.create_all()

@app.route('/')
def index():
  postList = Post.query.order_by(Post.timestamp).all()
  return render_template('posts.html', postList=postList)

@app.route('/addPost', methods=['POST'])
def handlePost():
  content = request.form['content']
  print(content)
  new_post = Post(content=content, username="anonymous")
  try:
    db.session.add(new_post)
    db.session.commit()
    return redirect('/')
  except:
    return redirect('/')

@app.route('/createAccount', methods=['POST'])
def handleCreateAccount():
  formData = request.get_json()
  #Lookup username
  accNameQuery = Account.query.filter_by(username=formData['createUsername']).first()
  if not (accNameQuery is None):
    return Response("Username already in use", 400)
  #Check passwords
  if formData['createPassword'] != formData['verifyPassword']:
    return Response("Passwords don't match", 400)
  #create Account
  newAccount = Account(username=formData['createUsername'], password=formData['createPassword'])
  db.session.add(newAccount)
  db.session.commit()

  return jsonify({'status': 'success'})

@app.route('/loginAuth', methods=['POST', 'GET'])
def handeLogin():
  formData = request.get_json()
  accountLookup = Account.query.filter_by(username=formData['username']).first()
  if accountLookup is None:
    return Response("Username doesn't exist", 401)
  if accountLookup.password != formData['password']:
    return Response("Password is incorrect", 401)
  user = User()
  user.id = accountLookup.id
  access_token = create_access_token(identity=user.id)
  response = jsonify(access_token=access_token)
  return response, 200

"""
Check if user matches userId
"""
def check_user(username, userId):
  accountLookup = Account.query.filter_by(username=username)
  if accountLookup is None:
    return False
  if accountLookup.id != userId:
    return False
  return True

@app.route('/protected')
@jwt_required
def protected():
  current_user = get_jwt_identity()
  print(current_user)
  return jsonify(logged_in_as=current_user), 200
  #return render_template("loggedin.html", user=flask_login.current_user)

@app.route('/home', methods = ['GET'])
@jwt_required
def loadHomeData():
  current_user = get_jwt_identity()
  data = {
    'field1': 'foo',
    'field2': 'bar',
    'field2': 'baz'
  }
  return jsonify(data), 200
  #return render_template("loggedin.html", user=flask_login.current_user)
"""
Flask-login code here
"""

# Helper account lookups
def lookupUser(username):
  accountLookup = Account.query.filter_by(username=username).first()
  if accountLookup is None:
    return None
  return accountLookup

def checkPassword(username, password):
  accountLookup = Account.query.filter_by(username=username).first()
  if accountLookup is None:
    return False
  if accountLookup.password == password:
    return True
  return False

@jwt.token_in_blacklist_loader
def checkTokenBlacklist(token):
  print(token)
  jti = token['jti']
  return jti in blacklist

@app.route('/logout', methods = ['GET'])
@jwt_required
def logout():
    print("foobar")
    jti = get_raw_jwt()['jti']
    print(jti)
    blacklist.add(jti)
    return Response("Success", 200)

#backend template for login page
@app.route('/loginPage', methods = ['GET', 'POST'])
def loginPage():
  if request.method == 'GET':
    return render_template('login.html')
  
  username = request.form['username']
  password = request.form['password']
  lookup =  checkPassword(username, password)
  if lookup:
    user = User()
    user.id = username
    return redirect('/protected')
  else:
    return Response("Passwords don't match", 400)

"""
Backend call to find users
"""
@app.route('/findUsers', methods = ['GET'])
def findUsers():
  userLookup = Account.query.all()
  respQuery = {'users': []}
  for user in userLookup:
    userData = {
      'id': user.id,
      'username': user.username,
    }
    respQuery['users'].append(userData)
  return jsonify(respQuery)

"""
Backend call to follow another user
"""
@app.route('/followUser', methods=['POST'])
def followUser():
  return response("wip", 400)

if __name__ == '__main__':
    app.run(debug=True)