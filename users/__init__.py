from flask import Blueprint

# Create a Blueprint for the users module
users_bp = Blueprint("users", __name__)

from . import routes  # Import routes to register them with the blueprint
