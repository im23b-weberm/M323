"""
Main Flask application for Todo API with user authentication.
"""

from flask import Flask, jsonify, request
from flask_login import LoginManager, login_user, logout_user, login_required
from todo_Item import TodoItem
from todo_Dao import TodoDao
from user_dao import UserDao

app = Flask(__name__)
app.secret_key = 'super-secret-key'  # consistent single quotes

# Initialize DAOs
todo_dao = TodoDao('todo_example.db')
user_dao = UserDao()

# Setup Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return user_dao.get_user_by_id(int(user_id))


@app.route('/todos', methods=['POST'])
@login_required
def add_todo():
    data = request.get_json()
    new_item = TodoItem(None, data['title'], data['is_completed'])
    todo_dao.add_item(new_item)
    return jsonify({'message': 'Todo item created'}), 201


@app.route('/todos', methods=['GET'])
@login_required
def get_all_todos():
    items = todo_dao.get_all_items()
    return jsonify([item.__dict__ for item in items]), 200


@app.route('/todos/<int:item_id>', methods=['GET'])
@login_required
def get_todo(item_id):
    item = todo_dao.get_item(item_id)
    if item:
        return jsonify(item.__dict__), 200
    return jsonify({'message': 'Item not found'}), 404


@app.route('/todos/<int:item_id>', methods=['PUT'])
@login_required
def update_todo(item_id):
    data = request.get_json()
    updated_item = TodoItem(item_id, data['title'], data['is_completed'])
    if todo_dao.update_item(updated_item):
        return jsonify({'message': 'Item updated'}), 200
    return jsonify({'message': 'Item not found or not updated'}), 404


@app.route('/todos/<int:item_id>', methods=['DELETE'])
@login_required
def delete_todo(item_id):
    if todo_dao.delete_item(item_id):
        return jsonify({'message': 'Item deleted'}), 200
    return jsonify({'message': 'Item not found or not deleted'}), 404


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Username and password required', 'status': 'error'}), 400

    username = data['username']
    password = data['password']

    # Use global user_dao, do not redefine
    user = user_dao.get_user_by_username(username)

    # Create user if not exists
    if user is None:
        user = user_dao.create_user(username, password)
        login_user(user)
        return jsonify({'message': 'User created and logged in', 'status': 'success', 'user_id': user.get_id()}), 201

    # Check password
    if user.password != password:
        return jsonify({'message': 'Invalid username or password', 'status': 'error'}), 401

    login_user(user)
    return jsonify({
        'success': True,
        'message': 'Login successful',
        'user_id': user.get_id()
    }), 200

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful', 'status': 'success'}), 200


def generate_testdata():
    """Generate sample todos for testing purposes."""
    todo_dao.create_table()
    todo_dao.add_item(TodoItem(1, 'Buy milk', False))
    todo_dao.add_item(TodoItem(2, 'Buy eggs', False))
    todo_dao.add_item(TodoItem(3, 'Buy bread', False))
    todo_dao.add_item(TodoItem(4, 'Buy butter', False))


if __name__ == '__main__':
    generate_testdata()
    app.run()
