from flask import Blueprint, request, jsonify
from app import db
from tasks.models import Task
from flask_jwt_extended import jwt_required, get_jwt_identity

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route("/", methods=["POST"])
@jwt_required()
def create_task():
    data = request.json
    task = Task(
        title=data["title"],
        description=data.get("description"),
        due_date=data.get("due_date"),
        user_id=get_jwt_identity(),
    )
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "Task created successfully"}), 201

@tasks_bp.route("/", methods=["GET"])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": task.id, "title": task.title, "status": task.status} for task in tasks])

@tasks_bp.route("/<int:task_id>", methods=["PUT"])
@jwt_required()
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.json
    task.status = data.get("status", task.status)
    db.session.commit()
    return jsonify({"message": "Task updated successfully"})

@tasks_bp.route("/<int:task_id>", methods=["DELETE"])
@jwt_required()
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully"})
