import os
from datetime import timedelta  # Import timedelta here

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:admin@localhost/blog')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your_secret_key'  
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)

