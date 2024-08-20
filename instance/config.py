import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')  # Default value should be secure for development
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///default.db')  # Default value for development
    SQLALCHEMY_TRACK_MODIFICATIONS = False
