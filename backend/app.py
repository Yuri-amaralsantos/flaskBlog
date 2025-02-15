from flask import Flask
from config import Config
from flask_migrate import Migrate
from extensions import db, bcrypt, jwt
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Configure CORS to allow specific methods for the blog routes
    CORS(app, resources={r"/*": {
        "origins": "http://localhost:5173",  # The frontend origin
        "methods": ["GET", "POST", "PUT", "DELETE"],  # Allow DELETE method
        "allow_headers": ["Content-Type", "Authorization"],  # Allow specific headers
    }})

    # Inicializando as extensões
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Inicializando o Flask-Migrate
    migrate = Migrate(app, db)  # Adiciona o Flask-Migrate ao aplicativo

    # Configurando o contexto da aplicação
    with app.app_context():
        from models import User, Post  # Importando os modelos
        # db.create_all()  # Isso é para criar as tabelas diretamente, mas é melhor usar migrações

    # Registrando os blueprints
    from routes.auth import auth_bp
    from routes.blog import blog_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(blog_bp, url_prefix='/blog')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
