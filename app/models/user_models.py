from app.database.db import get_connection

class User:
    # ==================== FETCH BY ID ====================
    @staticmethod
    def fetch_by_id(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        return cursor.fetchone()
    # ==================== CHANGE PASSWORD BY ID ====================
    @staticmethod
    def change_password_by_id(password, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET password = %s WHERE id = %s", (password, id))
        conn.commit()
        cursor.close()
        conn.close()
        return cursor.rowcount
    # ==================== UPDATE USER PROFILE BY ID ====================
    @staticmethod
    def update_user_profile_by_id(firstName, lastName, email, mobileNumber, city, address, country, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET firstName = %s, lastName = %s, email = %s, mobileNumber = %s, city = %s, address = %s, country = %s WHERE id = %s", (firstName, lastName, email, mobileNumber, city, address, country, id))
        conn.commit()
        cursor.close()
        conn.close()
        return cursor.rowcount
    # ==================== UPDATE USER BUISNESS PROFILE BY ID ====================
    @staticmethod
    def update_user_buisness_by_id(company, buisnessCategory, buisnessType, description, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET company = %s, buisnessCategory = %s, buisnessType = %s, description = %s WHERE id = %s", (company, buisnessCategory, buisnessType, description, id))
        conn.commit()
        cursor.close()
        conn.close()
        return cursor.rowcount