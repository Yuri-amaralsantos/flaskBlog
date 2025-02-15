# app.py
from flask import Flask
from config import Config
from extensions import db, bcrypt, jwt
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)


    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

   
    with app.app_context():
        from models import User, Post  
        db.create_all()

    from routes.auth import auth_bp
    from routes.blog import blog_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(blog_bp, url_prefix='/blog')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
