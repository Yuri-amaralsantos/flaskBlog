from flask import Blueprint, request, jsonify
from extensions import db
from models import Post, User, Comment
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

    comments = Comment.query.filter_by(post_id=post_id).all()
    comments_data = [{
        'id': comment.id,
        'content': comment.content,
        'author': comment.author_username,
        'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S')
    } for comment in comments]

    post_data = {
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'author': post.author.username if post.author else 'Unknown',
        'created_at': post.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        'comments': comments_data
    }

    return jsonify(post_data), 200

@blog_bp.route('/<int:post_id>', methods=['PUT'])
@jwt_required()
def edit_post(post_id):
    data = request.get_json()
    if not data or not data.get('title') or not data.get('content'):
        return jsonify({"message": "Invalid data"}), 400

    current_username = get_jwt_identity()  # Get the logged-in user (username)

    post = Post.query.get(post_id)
    if not post:
        return jsonify({"message": "Post not found"}), 404

    if post.author_username != current_username:
        return jsonify({"message": "Unauthorized"}), 403  # Prevents editing by others

    # Update post fields
    post.title = data['title']
    post.content = data['content']
    db.session.commit()

    return jsonify({"message": "Post updated successfully!"}), 200



#comments
@blog_bp.route('/<int:post_id>/comments', methods=['POST'])
@jwt_required()
def add_comment(post_id):
    data = request.get_json()
    if not data or not data.get('content'):
        return jsonify({"message": "Invalid data"}), 400

    current_username = get_jwt_identity()

    post = Post.query.get(post_id)
    if not post:
        return jsonify({"message": "Post not found"}), 404

    new_comment = Comment(
        content=data['content'],
        author_username=current_username,
        post_id=post_id
    )

    db.session.add(new_comment)
    db.session.commit()

    return jsonify({"message": "Comment added successfully!"}), 201

@blog_bp.route('/<int:post_id>/comments', methods=['GET'])
def get_comments(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"message": "Post not found"}), 404

    comments = Comment.query.filter_by(post_id=post_id).all()
    output = []
    for comment in comments:
        comment_data = {
            'id': comment.id,
            'content': comment.content,
            'author': comment.author_username,
            'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        output.append(comment_data)

    return jsonify(output), 200

@blog_bp.route('/comments/<int:comment_id>', methods=['DELETE'])
@jwt_required()
def delete_comment(comment_id):
    current_username = get_jwt_identity()

    comment = Comment.query.get(comment_id)
    if not comment:
        return jsonify({"message": "Comment not found"}), 404

    if comment.author_username != current_username:
        return jsonify({"message": "Unauthorized"}), 403

    db.session.delete(comment)
    db.session.commit()
    return jsonify({"message": "Comment deleted successfully!"}), 200
