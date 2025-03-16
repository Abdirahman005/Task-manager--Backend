from flask import Blueprint

# Create a Blueprint for the tasks module
tasks_bp = Blueprint("tasks", __name__)

from . import routes  # Import routes to register them with the blueprint
