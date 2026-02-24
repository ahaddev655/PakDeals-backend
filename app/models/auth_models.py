from app.database.db import get_connection

class Auth:
    @staticmethod
    def create_user(firstName, lastName, email, password, token, is_google_user=False):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO users (firstName, lastName, email, password, token, is_google_user) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (firstName, lastName, email, password, token, is_google_user))
        conn.commit()
        cursor.close()
        conn.close()
        return cursor.lastrowid

    @staticmethod
    def find_by_email(email):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        conn.commit()
        cursor.close()
        conn.close()
        return cursor.fetchone()
