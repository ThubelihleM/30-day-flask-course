from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)

# In-memory storage for todos
todos = [
  { 'id': 1, 'task': 'Learn Flask', 'done': False },
  { 'id': 2, 'task': 'Build API', 'done': False }
]

@api.route('/api/hello', methods=['GET'])
def hello():
  data = {'message': 'Hello from API', 'status': 'success'}
  return jsonify(data)

@api.route('/api/todos', methods=['GET'])
def get_todos():
  return jsonify(todos)

@api.route('/api/todos', methods=['POST'])
def add_todo():
  if not request.json or 'task' not in request.json:
    return jsonify({'error': 'Task is required'}), 400
  new_todo = {
    'id': len(todos) + 1,
    'task': request.json['task'],
    'done': False
  }
  todos.append(new_todo)
  return jsonify(new_todo)

@api.route('/api/todos/<int:id>', methods=['GET'])
def get_todo(id):
  todo = next((t for t in todos if t['id'] == id), None)
  if not todo:
    return jsonify({'error': 'Todo not found'}), 404
  return jsonify(todo)

@api.route('/api/todos/<int:id>', methods=['PUT'])
def update_todo(id):
  if not request.json or 'done' not in request.json:
    return jsonify({'error': 'Done status required'}), 400
  todo = next((t for t in todos if t['id'] == id), None)
  if not todo:
    return jsonify({'error': 'Todo not found'}), 404
  todo['done'] = request.json['done']
  return jsonify(todo)

@api.route('/api/fruits')
def get_fruits():
  return jsonify({'fruits': ['Apple', 'Banana', 'Orange', 'Mango']})