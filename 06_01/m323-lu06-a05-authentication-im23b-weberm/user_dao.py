import sqlite3
from user import User


class UserDao:
    def __init__(self, db_path="users.db"):
        self.db_path = db_path
        self._create_table()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    def get_user_by_id(self, user_id):
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, username, password FROM users WHERE id = ?",
            (user_id,)
        )

        row = cursor.fetchone()
        conn.close()

        if row:
            return User(row[0], row[1], row[2])
        return None

    def get_user_by_username(self, username):
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, username, password FROM users WHERE username = ?",
            (username,)
        )

        row = cursor.fetchone()
        conn.close()

        if row:
            return User(row[0], row[1], row[2])
        return None

    def create_user(self, username, password):
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )

        user_id = cursor.lastrowid
        conn.commit()
        conn.close()

        return User(user_id, username, password)
