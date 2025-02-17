# models.py
from extensions import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Use id as the primary key
    username = db.Column(db.String(80), unique=True, nullable=False)  # Ensure username is unique
    password = db.Column(db.String(200), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    user_posts = db.relationship('Post', back_populates='user', overlaps="author,posts")

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_username = db.Column(db.String(80), db.ForeignKey('user.username'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # Adding created_at
    user = db.relationship('User', back_populates='user_posts', overlaps="author,posts")
    # Relationship with User
