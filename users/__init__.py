from flask import Blueprint

users_bp = Blueprint("users", __name__)

from . import routes  # Import routes to register them with the blueprint
