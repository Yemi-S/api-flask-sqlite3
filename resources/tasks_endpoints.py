from flask import Blueprint, Flask, request,jsonify, Blueprint;
from datetime import datetime;
from database import tasks, setup;

tasks_bp = Blueprint('routes-tasks',__name__);

@tasks_bp.route('/tasks', methods=['POST'])
def add_task():
    title = request.json['title'];
    # Formato de fecha mm/dd/yyyy
    created_date = datetime.now().strftime("%x"); 
    data = (title, created_date);
    task_id = tasks.insert_task(data);

    if task_id:
        task = tasks.select_task_by_id(task_id);
        return jsonify({'task': task});
    return jsonify({'error': 'Internal error'});

@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    data = tasks.select_all_tasks();
    if data:
        return jsonify({'tasks': data});
    elif data == False:
        return jsonify({'error': "Internal error"});
    else:
        return jsonify({'tasks':{}});

@tasks_bp.route('/tasks', methods=['PUT'])
def update_task():
    title = request.json['title'];
    id_arg = request.args.get('id');

    if tasks.update_task(id_arg, (title,)):
        task = tasks.select_task_by_id(id_arg);
        return jsonify({'task': task});
    return jsonify({'error': "Internal error"});

@tasks_bp.route('/tasks', methods=['DELETE'])
def delete_task():
    id_arg = request.args.get('id');

    if tasks.delete_task(id_arg):
        return jsonify({'message': 'Task deleted'}); 
    return jsonify({'error': "Internal error"});

@tasks_bp.route('/tasks/completed', methods=['PUT'])
def completed_task():
    id_arg = request.args.get('id');
    completed_arg = request.args.get('completed');

    if tasks.complete_task(id_arg, completed_arg):
        return jsonify({'message': 'Successfully'}); 
    return jsonify({'error': "Internal error"});