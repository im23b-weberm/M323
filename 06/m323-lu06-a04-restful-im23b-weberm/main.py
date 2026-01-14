"""
flasking and todoing
"""
from flask import Flask, jsonify, request
from todo_Item import TodoItem
from todo_Dao import TodoDao


# Flask App initialisieren und TodoDao-Objekt erstellen
app = Flask(__name__)
dao = TodoDao('todo_example.db')
dao.create_table()


@app.route('/todos', methods=['POST'])
def add_todo():
    # TODO: Implementiere das Hinzufügen eines neuen ToDo-Elements
    data = request.get_json()
    new_item = TodoItem(None, data['title'], data['is_completed'])
    dao.add_item(new_item)
    return jsonify({'message': 'Todo item created'}), 201


@app.route('/todos', methods=['GET'])
def get_all_todos():
    # TODO: Implementiere das Abrufen aller ToDo-Elemente
    return jsonify(dao.get_all_items()), 200


@app.route('/todos/<int:item_id>', methods=['GET'])
def get_todo(item_id):
    # TODO: Implementiere das Abrufen eines einzelnen ToDo-Elements
    item = dao.get_item(item_id)
    if item:
        return jsonify(item), 200
    else:
        return jsonify({'message': 'Item not found'}), 404


@app.route('/todos/<int:item_id>', methods=['PUT'])
def update_todo(item_id):
    # TODO: Implementiere das Aktualisieren eines ToDo-Elements
    data = request.get_json()
    updated_item = TodoItem(item_id, data['title'], data['is_completed'])
    if dao.update_item(updated_item):
        return jsonify({'message': 'Item updated'}), 200
    else:
        return jsonify({'message': 'Item not found or not updated'}), 404


@app.route('/todos/<int:item_id>', methods=['DELETE'])
def delete_todo(item_id):
    # TODO: Implementiere das Löschen eines ToDo-Elements
    if dao.delete_item(item_id):
        return jsonify({'message': 'Item deleted'}), 200
    else:
        return jsonify({'message': 'Item not found or not deleted'}), 404


if __name__ == '__main__':
    app.run(debug=True)
