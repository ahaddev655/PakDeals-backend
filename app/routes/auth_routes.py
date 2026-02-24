from flask import Blueprint
from ..controllers.auth_controller import AuthController

auth_bp = Blueprint('auth', __name__, url_prefix="/api/auth")

# -------------------- SIMPLE ROUTES --------------------
auth_bp.route('/register', methods=['POST'])(AuthController.register)
auth_bp.route('/login', methods=['POST'])(AuthController.login)
# -------------------- GOOGLE ROUTES --------------------
auth_bp.route('/google-register', methods=['POST'])(AuthController.google_register)
auth_bp.route('/google-login', methods=['POST'])(AuthController.google_login )