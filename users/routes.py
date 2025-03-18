from flask import Blueprint, request, jsonify
from extensions import db
from users.models import User
from flask_jwt_extended import create_access_token

users_bp = Blueprint("users", __name__)

@users_bp.route("/register", methods=["POST"])
def register():
    data = request.json

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"message": "Email already exists"}), 400

    # Create new user and hash password
    user = User(username=data["username"], email=data["email"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

@users_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()

    # Validate user and password
    if user and user.check_password(data["password"]):
        token = create_access_token(identity=user.id)
        return jsonify({"token": token}), 200

    return jsonify({"message": "Invalid credentials"}), 401