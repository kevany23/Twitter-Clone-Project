from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
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

if __name__ == '__main__':
    app.run(debug=True)