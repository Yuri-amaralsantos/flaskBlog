# routes/auth.py
from flask import Blueprint, request, jsonify
from extensions import db, bcrypt
from models import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"message": "Invalid data"}), 400

    # Check if the username already exists
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"message": "Username already exists"}), 400
    
    # Get role from the request data, default to 'user' if not provided
    role = data.get('role', 'user')

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    # Create a new user with the given role
    new_user = User(username=data['username'], password=hashed_password, role=role)
    
    # Add the new user to the database and commit
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.username)  # Use username as identity
        return jsonify({
            "access_token": access_token,
            "username": user.username,
            "role": user.role  # Add role to the response
        }), 200
    
    return jsonify({"message": "Invalid credentials"}), 401




@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()  # Agora retorna o ID do usuário
    return jsonify({"message": f"Hello, user with ID {current_user_id}!"})

@auth_bp.route('/check_token', methods=['GET'])
@jwt_required()
def check_token():
    return jsonify({"valid": True})
