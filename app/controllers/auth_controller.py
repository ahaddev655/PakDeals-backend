from flask import request, jsonify
from app.models.auth_models import Auth
from secrets import token_hex
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


class AuthController:
    # ==================== REGISTER CONTROLLER ====================
    @staticmethod
    def register():
        try:
            data = request.get_json()
            firstName = data.get("firstName")
            lastName = data.get("lastName")
            email = data.get("email")
            password = data.get("password")

            if not all([firstName, lastName, email, password]):
                return jsonify({"error": "All fields are required"}), 400

            user = Auth.find_by_email(email)
            if user:
                return jsonify({"error": "User already exists"}), 401

            token = token_hex(16)
            hashedPassword = bcrypt.generate_password_hash(password).decode("utf-8")
            newUser = Auth.create_user(
                firstName, lastName, email, hashedPassword, token, is_google_user=False
            )

            return (
                jsonify(
                    {
                        "message": "User registered successfully",
                        "id": newUser,
                        "token": token,
                    }
                ),
                201,
            )

        except Exception as e:
            print(e)
            return jsonify({"details": str(e), "error": "Internal Server Error"}), 500

    # ==================== LOGIN CONTROLLER ====================
    @staticmethod
    def login():
        try:
            data = request.get_json()
            email = data.get("email")
            password = data.get("password")

            if not all([email, password]):
                return jsonify({"error": "Email and password are required"}), 400

            user = Auth.find_by_email(email)
            if not user:
                return jsonify({"error": "User not found"}), 401

            if user.get("is_google_user"):
                return jsonify({"error": "Please login using Google"}), 403

            if not bcrypt.check_password_hash(user["password"], password):
                return jsonify({"error": "Incorrect password"}), 401

            return (
                jsonify(
                    {
                        "message": "Login successful",
                        "token": user["token"],
                        "id": user["id"],
                    }
                ),
                200,
            )

        except Exception as e:
            return jsonify({"details": str(e), "error": "Internal Server Error"}), 500

    # ==================== GOOGLE REGISTER CONTROLLER ====================
    @staticmethod
    def google_register():
        try:
            data = request.get_json()
            firstName = data.get("firstName")
            lastName = data.get("lastName")
            email = data.get("email")
            password = data.get("password")

            if not all([firstName, lastName, email, password]):
                return jsonify({"error": "All fields are required"}), 400

            user = Auth.find_by_email(email)
            if user:
                return jsonify({"error": "User already exists"}), 401

            token = token_hex(16)
            hashedPassword = bcrypt.generate_password_hash(password).decode("utf-8")
            newUser = Auth.create_user(
                firstName, lastName, email, hashedPassword, token, is_google_user=True
            )

            return (
                jsonify(
                    {
                        "message": "User registered successfully",
                        "id": newUser,
                        "token": token,
                    }
                ),
                201,
            )

        except Exception as e:
            return jsonify({"details": str(e), "error": "Internal Server Error"}), 500

    # ==================== GOOGLE LOGIN CONTROLLER ====================
    @staticmethod
    def google_login():
        try:
            data = request.get_json()
            email = data.get("email")

            if not email:
                return jsonify({"error": "Email is required"}), 400

            user = Auth.find_by_email(email)
            if not user:
                return jsonify({"error": "User not found"}), 404

            if not user.get("is_google_user"):
                return (
                    jsonify({"error": "This email is not registered with Google"}),
                    403,
                )

            return (
                jsonify(
                    {
                        "message": "Login successful",
                        "user": {"id": user["id"], "token": user["token"]},
                    }
                ),
                200,
            )

        except Exception as e:
            return jsonify({"details": str(e), "error": "Internal Server Error"}), 500
