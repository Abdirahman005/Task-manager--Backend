import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from extensions import db, bcrypt, jwt
from users.routes import users_bp

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configuration using environment variables
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///users.db')  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your-secret-key')

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    CORS(app)  # Enable CORS

    # Register blueprints
    app.register_blueprint(users_bp, url_prefix='/api')

    return app  # Gunicorn will call create_app()

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()  # Ensure tables exist (only for development)
    app.run(debug=True, port=5000)
