from flask import Blueprint, request, jsonify
from extensions import db
from models import Post, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

blog_bp = Blueprint('blog_bp', __name__)

@blog_bp.route('/', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    output = []
    for post in posts:
        post_data = {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'author': post.author.username if post.author else 'Unknown',
            'created_at': post.created_at.strftime('%Y-%m-%d %H:%M:%S')  
        }
        output.append(post_data)
    return jsonify(output)

@blog_bp.route('/', methods=['POST'])
@jwt_required()
def create_post():
    data = request.get_json()
    if not data or not data.get('title') or not data.get('content'):
        return jsonify({"message": "Invalid data"}), 400

    current_username = get_jwt_identity()  # Now gets the username from JWT
    new_post = Post(
        title=data['title'],
        content=data['content'],
        author_username=current_username,
        created_at=datetime.utcnow()  # Adiciona o timestamp de criação
    )

    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created successfully!"}), 201

@blog_bp.route('/<int:post_id>', methods=['DELETE'])
@jwt_required()
def delete_post(post_id):
    current_username = get_jwt_identity()  # Get logged-in user (username)
   
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"message": "Post not found"}), 404

    if post.author_username != current_username:
        return jsonify({"message": "Unauthorized"}), 403  # Prevents deletion by others

    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Post deleted successfully!"}), 200

@blog_bp.route('/<int:post_id>', methods=['GET'])
def get_post_detail(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"message": "Post not found"}), 404

    post_data = {
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'author': post.author.username if post.author else 'Unknown',
        'created_at': post.created_at.strftime('%Y-%m-%d %H:%M:%S')
    }

    return jsonify(post_data), 200
