from flask import Blueprint, jsonify, request
from models import db, Task

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@tasks_bp.route('/', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(
        title=data.get('title'),
        description=data.get('description'),
        status=data.get('status', 'pending')
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

@tasks_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted"})
    return jsonify({"error": "Task not found"}), 404
