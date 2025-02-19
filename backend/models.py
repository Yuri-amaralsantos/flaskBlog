from extensions import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Use id as the primary key
    username = db.Column(db.String(80), unique=True, nullable=False)  # Ensure username is unique
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(10), nullable=False, default='user')  # Role field with default as 'user'

    posts = db.relationship('Post', backref='author', lazy=True)
    user_posts = db.relationship('Post', back_populates='user', overlaps="author,posts")

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_username = db.Column(db.String(80), db.ForeignKey('user.username'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # Adding created_at
    user = db.relationship('User', back_populates='user_posts', overlaps="author,posts")

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    author_username = db.Column(db.String(80), db.ForeignKey('user.username'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    post = db.relationship('Post', back_populates='comments')
    user = db.relationship('User')

Post.comments = db.relationship('Comment', back_populates='post', lazy=True, cascade="all, delete-orphan")

