from flask import Blueprint
from ..controllers.user_controller import UserController

user_bp = Blueprint("users", __name__, url_prefix="/api/users")

user_bp.route("/fetch-user/<int:id>", methods=["GET"])(
    UserController.personalUserProfile
)
user_bp.route("/update-password/<int:id>", methods=["PUT"])(
    UserController.changePassword
)
user_bp.route("/update-personal-profile/<int:id>", methods=["PUT"])(
    UserController.updateUserProfile
)
user_bp.route("/update-buisness-profile/<int:id>", methods=["PUT"])(
    UserController.updateBuisnessProfile
)
