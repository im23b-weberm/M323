from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password  # hashed password!

    def __repr__(self):
        return f"<User {self.username}>"
