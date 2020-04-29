from flask import Flask, render_template, request, redirect, jsonify, Response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

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
    print("Username already used")
    return Response("Username already in use", 400)
  #Check passwords
  if formData['createPassword'] != formData['verifyPassword']:
    return Response("Passwords don't match", 400)
  #create Account
  newAccount = Account(username=formData['createUsername'], password=formData['createPassword'])
  db.session.add(newAccount)
  db.session.commit()

  return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)