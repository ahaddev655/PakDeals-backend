from flask import jsonify, request
from app.models.user_models import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class UserController:
    # ==================== FETCH USER BY ID ====================
    @staticmethod
    def personalUserProfile(id):
        try:
            user = User.fetch_by_id(id)

            if not user:
                return jsonify({"error": "User not found"}), 401

            return jsonify({"message": "User fetched successfully", "user": user}), 200
        except Exception as e:
            print(e)
            return jsonify({"details": str(e), "error": "Internal Server Error"}), 500
    # ==================== UPDATE PASSWORD BY ID ====================
    @staticmethod
    def changePassword(id):
        try:
            data = request.get_json()
            newPassword = data.get("newPassword")
            user = User.fetch_by_id(id)

            hashed_password = bcrypt.generate_password_hash(newPassword).decode('utf-8')

            User.change_password_by_id(hashed_password, id)

            if not user:
                return jsonify({"error": "User not found"}), 401

            return jsonify({"message": "Password updated successfully"}), 200
        except Exception as e:
            print(e)
            return jsonify({"details": str(e), "error": "Internal Server Error"}), 500
    
        # ==================== UPDATE USER PROFILE BY ID ====================
    @staticmethod
    def updateUserProfile(id):
        try:
            data = request.get_json()
            firstName = data.get("firstName")
            lastName = data.get("lastName")
            email = data.get("email")
            mobileNumber = data.get("mobileNumber")
            city = data.get("city")
            address = data.get("address")
            country = data.get("country")

            user = User.fetch_by_id(id)
            if not user:
                return jsonify({"error": "User not found"}), 401

            User.update_user_profile_by_id(firstName, lastName, email, mobileNumber, city, address, country, id)

            return jsonify({"message": "Personal profile successfully"}), 200
        except Exception as e:
            print(e)
            return jsonify({"details": str(e), "error": "Internal Server Error"}), 500
    
        # ==================== UPDATE USER BUISNESS PROFILE BY ID ====================
    @staticmethod
    def updateBuisnessProfile(id):
        try:
            data = request.get_json()
            company = data.get("company")
            description = data.get("description")
            buisnessCategory = data.get("buisnessCategory")
            buisnessType = data.get("buisnessType")

            user = User.fetch_by_id(id)
            if not user:
                return jsonify({"error": "User not found"}), 401

            User.update_user_buisness_by_id(company, buisnessCategory, buisnessType, description, id)

            return jsonify({"message": "Buisness profile updated"}), 200
        except Exception as e:
            print(e)
            return jsonify({"details": str(e), "error": "Internal Server Error"}), 500