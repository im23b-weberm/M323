"""
doc
"""
from flask import Flask
from flask_login import LoginManager

from todo_Blueprint import todo_blueprint
from user_Blueprint import user_blueprint
from todo_Item import TodoItem
from user import User
from todo_Dao import TodoDao
from user_Dao import UserDao

app = Flask(__name__)
app.secret_key = 'supersecretkey'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    from user_Dao import UserDao

    user_dao = UserDao('todo_example.db')
    return user_dao.get_user_by_id(int(user_id))


app.register_blueprint(todo_blueprint)
app.register_blueprint(user_blueprint)


def generate_testdata():

    todo_dao = TodoDao('todo_example.db')
    user_dao = UserDao('todo_example.db')

    # Generate user
    user_dao.create_user_table()
    user_dao.add_user(User(1, 'admin', 'admin@example', 'admin'))
    user_dao.add_user(User(2, 'user', 'user@example', 'user'))

    # Generate todo items
    todo_dao.create_table()
    todo_dao.add_item(TodoItem(1, 1, 'Buy milk', False))
    todo_dao.add_item(TodoItem(2, 1, 'Buy eggs', False))
    todo_dao.add_item(TodoItem(3, 2, 'Buy bread', False))
    todo_dao.add_item(TodoItem(4, 2, 'Buy butter', False))

    todo_dao.close()
    user_dao.close()


if __name__ == '__main__':
    generate_testdata()
    app.run(debug=True)

