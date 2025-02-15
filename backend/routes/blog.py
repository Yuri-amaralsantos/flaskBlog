# routes/blog.py
from flask import Blueprint, request, jsonify
from extensions import db
from models import Post, User
from flask_jwt_extended import jwt_required, get_jwt_identity

blog_bp = Blueprint('blog_bp', __name__)

@blog_bp.route('/', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    output = []
    for post in posts:
        post_data = {
            'title': post.title,
            'content': post.content,
            'author': post.author.username if post.author else 'Unknown'
        }
        output.append(post_data)
    return jsonify(output)

@blog_bp.route('/', methods=['POST'])
@jwt_required()
def create_post():
    data = request.get_json()
    if not data or not data.get('title') or not data.get('content'):
        return jsonify({"message": "Invalid data"}), 400

    current_user_id = int(get_jwt_identity())
    new_post = Post(title=data['title'], content=data['content'], user_id=current_user_id)
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created successfully!"}), 201
